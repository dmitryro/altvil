var AngularRemote;
(function (AngularRemote) {
    var lowercase = angular.lowercase;
    var isObject = angular.isObject;
    var isFunction = angular.isFunction;
    var isNumber = angular.isNumber;
    var isDefined = angular.isDefined;
    var isString = angular.isString;
    var forEach = angular.forEach;
    var extend = angular.extend;
    var noop = angular.noop;
    var OPERATORS = {
        'null': function () {
            return null;
        },
        'true': function () {
            return true;
        },
        'false': function () {
            return false;
        },
        undefined: angular.noop,
        '+': function (self, locals, a, b) {
            a = a(self, locals);
            b = b(self, locals);
            return (isDefined(a) ? a : 0) + (isDefined(b) ? b : 0);
        },
        '-': function (self, locals, a, b) {
            a = a(self, locals);
            b = b(self, locals);
            return (isDefined(a) ? a : 0) - (isDefined(b) ? b : 0);
        },
        '*': function (self, locals, a, b) {
            return a(self, locals) * b(self, locals);
        },
        '/': function (self, locals, a, b) {
            return a(self, locals) / b(self, locals);
        },
        '%': function (self, locals, a, b) {
            return a(self, locals) % b(self, locals);
        },
        '^': function (self, locals, a, b) {
            return a(self, locals) ^ b(self, locals);
        },
        '=': angular.noop,
        '==': function (self, locals, a, b) {
            return a(self, locals) == b(self, locals);
        },
        '!=': function (self, locals, a, b) {
            return a(self, locals) != b(self, locals);
        },
        '<': function (self, locals, a, b) {
            return a(self, locals) < b(self, locals);
        },
        '>': function (self, locals, a, b) {
            return a(self, locals) > b(self, locals);
        },
        '<=': function (self, locals, a, b) {
            return a(self, locals) <= b(self, locals);
        },
        '>=': function (self, locals, a, b) {
            return a(self, locals) >= b(self, locals);
        },
        '&&': function (self, locals, a, b) {
            return a(self, locals) && b(self, locals);
        },
        '||': function (self, locals, a, b) {
            return a(self, locals) || b(self, locals);
        },
        '&': function (self, locals, a, b) {
            return a(self, locals) & b(self, locals);
        },
        '|': function (self, locals, a, b) {
            return b(self, locals)(self, locals, a(self, locals));
        },
        '!': function (self, locals, a) {
            return !a(self, locals);
        }
    };
    var ESCAPE = {
        "n": "\n",
        "f": "\f",
        "r": "\r",
        "t": "\t",
        "v": "\v",
        "'": "'",
        '"': '"'
    };
    function lex(text, csp) {
        var tokens = [];
        var token;
        var index = 0;
        var json = [];
        var ch;
        var lastCh = ':';

        while(index < text.length) {
            ch = text.charAt(index);
            if(is('"\'')) {
                readString(ch);
            } else {
                if(isNumber(ch) || is('.') && isNumber(peek())) {
                    readNumber();
                } else {
                    if(isIdent(ch)) {
                        readIdent();
                        if(was('{,') && json[0] == '{' && (token = tokens[tokens.length - 1])) {
                            token.json = token.text.indexOf('.') == -1;
                        }
                    } else {
                        if(is('(){}[].,;:')) {
                            tokens.push({
                                index: index,
                                text: ch,
                                json: (was(':[,') && is('{[')) || is('}]:,')
                            });
                            if(is('{[')) {
                                json.unshift(ch);
                            }
                            if(is('}]')) {
                                json.shift();
                            }
                            index++;
                        } else {
                            if(isWhitespace(ch)) {
                                index++;
                                continue;
                            } else {
                                var ch2 = ch + peek();
                                var fn = OPERATORS[ch];
                                var fn2 = OPERATORS[ch2];

                                if(fn2) {
                                    tokens.push({
                                        index: index,
                                        text: ch2,
                                        fn: fn2
                                    });
                                    index += 2;
                                } else {
                                    if(fn) {
                                        tokens.push({
                                            index: index,
                                            text: ch,
                                            fn: fn,
                                            json: was('[,:') && is('+-')
                                        });
                                        index += 1;
                                    } else {
                                        throwError("Unexpected next character ", index, index + 1);
                                    }
                                }
                            }
                        }
                    }
                }
            }
            lastCh = ch;
        }
        return tokens;
        function is(chars) {
            return chars.indexOf(ch) != -1;
        }
        function was(chars) {
            return chars.indexOf(lastCh) != -1;
        }
        function peek() {
            return index + 1 < text.length ? text.charAt(index + 1) : false;
        }
        function isNumber(ch) {
            return '0' <= ch && ch <= '9';
        }
        function isWhitespace(ch) {
            return ch == ' ' || ch == '\r' || ch == '\t' || ch == '\n' || ch == '\v' || ch == '\u00A0';
        }
        function isIdent(ch) {
            return 'a' <= ch && ch <= 'z' || 'A' <= ch && ch <= 'Z' || '_' == ch || ch == '$';
        }
        function isExpOperator(ch) {
            return ch == '-' || ch == '+' || isNumber(ch);
        }
        function throwError(error, start, end) {
            end = end || index;
            throw Error("Lexer Error: " + error + " at column" + (isDefined(start) ? "s " + start + "-" + index + " [" + text.substring(start, end) + "]" : " " + end) + " in expression [" + text + "].");
        }
        function readNumber() {
            var num = "";
            var start = index;
            while(index < text.length) {
                var ch = lowercase(text.charAt(index));
                if(ch == '.' || isNumber(ch)) {
                    num += ch;
                } else {
                    var peekCh = peek();
                    if(ch == 'e' && isExpOperator(peekCh)) {
                        num += ch;
                    } else {
                        if(isExpOperator(ch) && peekCh && isNumber(peekCh) && num.charAt(num.length - 1) == 'e') {
                            num += ch;
                        } else {
                            if(isExpOperator(ch) && (!peekCh || !isNumber(peekCh)) && num.charAt(num.length - 1) == 'e') {
                                throwError('Invalid exponent');
                            } else {
                                break;
                            }
                        }
                    }
                }
                index++;
            }
            num = (1) * num;
            tokens.push({
                index: start,
                text: num,
                json: true,
                fn: function () {
                    return num;
                }
            });
        }
        function readIdent() {
            var ident = "";
            var start = index;
            var lastDot;
            var peekIndex;
            var methodName;

            while(index < text.length) {
                var ch = text.charAt(index);
                if(ch == '.' || isIdent(ch) || isNumber(ch)) {
                    if(ch == '.') {
                        lastDot = index;
                    }
                    ident += ch;
                } else {
                    break;
                }
                index++;
            }
            if(lastDot) {
                peekIndex = index;
                while(peekIndex < text.length) {
                    var ch = text.charAt(peekIndex);
                    if(ch == '(') {
                        methodName = ident.substr(lastDot - start + 1);
                        ident = ident.substr(0, lastDot - start);
                        index = peekIndex;
                        break;
                    }
                    if(isWhitespace(ch)) {
                        peekIndex++;
                    } else {
                        break;
                    }
                }
            }
            var token = {
                index: start,
                text: ident
            };
            if(OPERATORS.hasOwnProperty(ident)) {
                token.fn = token.json = OPERATORS[ident];
            } else {
                var getter = getterFn(ident, csp);
                token.fn = extend(function (self, locals) {
                    return (getter(self, locals));
                }, {
                    assign: function (self, value) {
                        return setter(self, ident, value);
                    }
                });
            }
            tokens.push(token);
            if(methodName) {
                tokens.push({
                    index: lastDot,
                    text: '.',
                    json: false
                });
                tokens.push({
                    index: lastDot + 1,
                    text: methodName,
                    json: false
                });
            }
        }
        function readString(quote) {
            var start = index;
            index++;
            var string = "";
            var rawString = quote;
            var escape = false;
            while(index < text.length) {
                var ch = text.charAt(index);
                rawString += ch;
                if(escape) {
                    if(ch == 'u') {
                        var hex = text.substring(index + 1, index + 5);
                        if(!hex.match(/[\da-f]{4}/i)) {
                            throwError("Invalid unicode escape [\\u" + hex + "]");
                        }
                        index += 4;
                        string += String.fromCharCode(parseInt(hex, 16));
                    } else {
                        var rep = ESCAPE[ch];
                        if(rep) {
                            string += rep;
                        } else {
                            string += ch;
                        }
                    }
                    escape = false;
                } else {
                    if(ch == '\\') {
                        escape = true;
                    } else {
                        if(ch == quote) {
                            index++;
                            tokens.push({
                                index: start,
                                text: rawString,
                                string: string,
                                json: true,
                                fn: function () {
                                    return string;
                                }
                            });
                            return;
                        } else {
                            string += ch;
                        }
                    }
                }
                index++;
            }
            throwError("Unterminated quote", start);
        }
    }
    function setter(obj, path, setValue) {
        var element = path.split('.');
        for(var i = 0; element.length > 1; i++) {
            var key = element.shift();
            var propertyObj = obj[key];
            if(!propertyObj) {
                propertyObj = {
                };
                obj[key] = propertyObj;
            }
            obj = propertyObj;
        }
        var key = element.shift();
        var oldValue = obj[key];
        obj[key] = setValue;
        if(!AngularRemote.HasNativeObserver()) {
            var cr = new AngularRemote.ChangeRecord("update", obj, key, oldValue);
        }
        return setValue;
    }
    function valueFn(value) {
        return function () {
            return value;
        }
    }
    function parser2(text, json, $filter, csp) {
        var ZERO = valueFn(0);
        var value;
        var tokens = lex(text, csp);
        var assignment = _assignment;
        var functionCall = _functionCall;
        var fieldAccess = _fieldAccess;
        var objectIndex = _objectIndex;
        var filterChain = _filterChain;

        if(json) {
            assignment = logicalOR;
            functionCall = fieldAccess = objectIndex = filterChain = function () {
                throwError("is not valid json", {
                    text: text,
                    index: 0
                });
            };
            value = primary();
        } else {
            value = statements();
        }
        if(tokens.length !== 0) {
            throwError("is an unexpected token", tokens[0]);
        }
        return value;
        function throwError(msg, token) {
            throw Error("Syntax Error: Token '" + token.text + "' " + msg + " at column " + (token.index + 1) + " of the expression [" + text + "] starting at [" + text.substring(token.index) + "].");
        }
        function peekToken() {
            if(tokens.length === 0) {
                throw Error("Unexpected end of expression: " + text);
            }
            return tokens[0];
        }
        function peek(e1, e2, e3, e4) {
            if(tokens.length > 0) {
                var token = tokens[0];
                var t = token.text;
                if(t == e1 || t == e2 || t == e3 || t == e4 || (!e1 && !e2 && !e3 && !e4)) {
                    return token;
                }
            }
            return false;
        }
        function expect(e1, e2, e3, e4) {
            var token = peek(e1, e2, e3, e4);
            if(token) {
                if(json && !token.json) {
                    throwError("is not valid json", token);
                }
                tokens.shift();
                return token;
            }
            return false;
        }
        function consume(e1) {
            if(!expect(e1)) {
                throwError("is unexpected, expecting [" + e1 + "]", peek());
            }
        }
        function unaryFn(fn, right) {
            return function (self, locals) {
                return fn(self, locals, right);
            }
        }
        function binaryFn(left, fn, right) {
            return function (self, locals) {
                return fn(self, locals, left, right);
            }
        }
        function statements() {
            var statements = [];
            while(true) {
                if(tokens.length > 0 && !peek('}', ')', ';', ']')) {
                    statements.push(filterChain());
                }
                if(!expect(';')) {
                    return statements.length == 1 ? statements[0] : function (self, locals) {
                        var value;
                        for(var i = 0; i < statements.length; i++) {
                            var statement = statements[i];
                            if(statement) {
                                value = statement(self, locals);
                            }
                        }
                        return value;
                    };
                }
            }
        }
        function _filterChain() {
            var left = expression();
            var token;
            while(true) {
                if((token = expect('|'))) {
                    left = binaryFn(left, token.fn, filter());
                } else {
                    return left;
                }
            }
        }
        function filter() {
            var token = expect();
            var fn = $filter(token.text);
            var argsFn = [];
            while(true) {
                if((token = expect(':'))) {
                    argsFn.push(expression());
                } else {
                    var fnInvoke = function (self, locals, input) {
                        var args = [
                            input
                        ];
                        for(var i = 0; i < argsFn.length; i++) {
                            args.push(argsFn[i](self, locals));
                        }
                        return fn.apply(self, args);
                    };
                    return function () {
                        return fnInvoke;
                    }
                }
            }
        }
        function expression() {
            return assignment();
        }
        function _assignment() {
            var left = logicalOR();
            var right;
            var token;
            if((token = expect('='))) {
                if(!left.assign) {
                    throwError("implies assignment but [" + text.substring(0, token.index) + "] can not be assigned to", token);
                }
                right = logicalOR();
                return function (self, locals) {
                    return left.assign(self, right(self, locals), locals);
                }
            } else {
                return left;
            }
        }
        function logicalOR() {
            var left = logicalAND();
            var token;
            while(true) {
                if((token = expect('||'))) {
                    left = binaryFn(left, token.fn, logicalAND());
                } else {
                    return left;
                }
            }
        }
        function logicalAND() {
            var left = equality();
            var token;
            if((token = expect('&&'))) {
                left = binaryFn(left, token.fn, logicalAND());
            }
            return left;
        }
        function equality() {
            var left = relational();
            var token;
            if((token = expect('==', '!='))) {
                left = binaryFn(left, token.fn, equality());
            }
            return left;
        }
        function relational() {
            var left = additive();
            var token;
            if((token = expect('<', '>', '<=', '>='))) {
                left = binaryFn(left, token.fn, relational());
            }
            return left;
        }
        function additive() {
            var left = multiplicative();
            var token;
            while((token = expect('+', '-'))) {
                left = binaryFn(left, token.fn, multiplicative());
            }
            return left;
        }
        function multiplicative() {
            var left = unary();
            var token;
            while((token = expect('*', '/', '%'))) {
                left = binaryFn(left, token.fn, unary());
            }
            return left;
        }
        function unary() {
            var token;
            if(expect('+')) {
                return primary();
            } else {
                if((token = expect('-'))) {
                    return binaryFn(ZERO, token.fn, unary());
                } else {
                    if((token = expect('!'))) {
                        return unaryFn(token.fn, unary());
                    } else {
                        return primary();
                    }
                }
            }
        }
        function primary() {
            var primary;
            if(expect('(')) {
                primary = filterChain();
                consume(')');
            } else {
                if(expect('[')) {
                    primary = arrayDeclaration();
                } else {
                    if(expect('{')) {
                        primary = object();
                    } else {
                        var token = expect();
                        primary = token.fn;
                        if(!primary) {
                            throwError("not a primary expression", token);
                        }
                    }
                }
            }
            var next;
            var context;

            while((next = expect('(', '[', '.'))) {
                if(next.text === '(') {
                    primary = functionCall(primary, context);
                    context = null;
                } else {
                    if(next.text === '[') {
                        context = primary;
                        primary = objectIndex(primary);
                    } else {
                        if(next.text === '.') {
                            context = primary;
                            primary = fieldAccess(primary);
                        } else {
                            throwError("IMPOSSIBLE");
                        }
                    }
                }
            }
            return primary;
        }
        function _fieldAccess(object) {
            var field = expect().text;
            var getter = getterFn(field, csp);
            return extend(function (self, locals) {
                return getter(object(self, locals), locals);
            }, {
                assign: function (self, value, locals) {
                    return setter(object(self, locals), field, value);
                }
            });
        }
        function _objectIndex(obj) {
            var indexFn = expression();
            consume(']');
            return extend(function (self, locals) {
                var o = obj(self, locals);
                var i = indexFn(self, locals);
                var v;
                var p;

                if(!o) {
                    return undefined;
                }
                v = o[i];
                if(v && v.then) {
                    p = v;
                    if(!('$$v' in v)) {
                        p.$$v = undefined;
                        p.then(function (val) {
                            p.$$v = val;
                        });
                    }
                    v = v.$$v;
                }
                return v;
            }, {
                assign: function (self, value, locals) {
                    return obj(self, locals)[indexFn(self, locals)] = value;
                }
            });
        }
        function _functionCall(fn, contextGetter) {
            var argsFn = [];
            if(peekToken().text != ')') {
                do {
                    argsFn.push(expression());
                }while(expect(','))
            }
            consume(')');
            return function (self, locals) {
                var args = [];
                var context = contextGetter ? contextGetter(self, locals) : self;

                for(var i = 0; i < argsFn.length; i++) {
                    args.push(argsFn[i](self, locals));
                }
                var fnPtr = fn(self, locals) || noop;
                return fnPtr.apply ? fnPtr.apply(context, args) : fnPtr(args[0], args[1], args[2], args[3], args[4]);
            }
        }
        function arrayDeclaration() {
            var elementFns = [];
            if(peekToken().text != ']') {
                do {
                    elementFns.push(expression());
                }while(expect(','))
            }
            consume(']');
            return function (self, locals) {
                var array = [];
                for(var i = 0; i < elementFns.length; i++) {
                    array.push(elementFns[i](self, locals));
                }
                return array;
            }
        }
        function object() {
            var keyValues = [];
            if(peekToken().text != '}') {
                do {
                    var token = expect();
                    var key = token.string || token.text;

                    consume(":");
                    var value = expression();
                    keyValues.push({
                        key: key,
                        value: value
                    });
                }while(expect(','))
            }
            consume('}');
            return function (self, locals) {
                var object = {
                };
                for(var i = 0; i < keyValues.length; i++) {
                    var keyValue = keyValues[i];
                    var value = keyValue.value(self, locals);
                    object[keyValue.key] = value;
                }
                return object;
            }
        }
    }
    AngularRemote.parser2 = parser2;
    var getterFnCache = {
    };
    function getterFn(path, csp) {
        if(getterFnCache.hasOwnProperty(path)) {
            return getterFnCache[path];
        }
        var pathKeys = path.split('.');
        var pathKeysLength = pathKeys.length;
        var fn;

        if(csp) {
            throw "CSP not supported";
        } else {
            var code = 'var l, fn, p;\n';
            forEach(pathKeys, function (key, index) {
                code += 'if(s === null || s === undefined) return s;\n' + 'l=s;\n' + 's=' + (index ? 's' : '((k&&k.hasOwnProperty("' + key + '"))?k:s)') + '["' + key + '"]' + ';\n' + 'if (s && s.then) {\n' + ' if (!("$$v" in s)) {\n' + ' p=s;\n' + ' p.$$v = undefined;\n' + ' p.then(function(v) {p.$$v=v;});\n' + '}\n' + ' s=s.$$v\n' + '}\n';
            });
            code += 'return s;';
            fn = Function('s', 'k', code);
            fn.toString = function () {
                return code;
            };
        }
        return getterFnCache[path] = fn;
    }
})(AngularRemote || (AngularRemote = {}));

