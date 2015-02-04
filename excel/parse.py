import xlrd
import psycopg2
import sys
import site

def is_number(s):
    try:
        float(s) # for int, long and float
    except ValueError:
        try:
            complex(s) # for complex
        except ValueError:
            return False

    return True


fname = raw_input('Enter the file name: ')
try:
    workbook = xlrd.open_workbook(fname)
    worksheet = workbook.sheet_by_name('households')
    num_rows = worksheet.nrows - 1
    curr_row = 1001
    print num_rows
    con = psycopg2.connect("dbname='geodjango' user='postgres'")
    cur = con.cursor()


    while curr_row < 1003:       
      try:
          print '----'
          row = worksheet.row(curr_row)
          
          household_id = worksheet.cell_value(curr_row, 0)
          service_area_id = worksheet.cell_value(curr_row, 1)
          address_street = worksheet.cell_value(curr_row, 2)
          address_city = worksheet.cell_value(curr_row, 3)
          address_state = worksheet.cell_value(curr_row, 4)
          address_zip = worksheet.cell_value(curr_row, 5)
          coordinates = worksheet.cell_value(curr_row, 6) 
          road_segment_id = worksheet.cell_value(curr_row, 7)
          road_segment_start_distance = worksheet.cell_value(curr_row, 8)   
          road_segment_end_distance = worksheet.cell_value(curr_row, 9)

          print household_id
          print service_area_id
          print address_street
          print address_city
          print address_state

          insertstmt=("INSERT  into geography_householdraw ( household_id, service_area_id, address_street,"+
                      " address_city, address_state, address_zip,"+
                      "coordinates, road_segment_id, road_segment_start_distance,road_segment_end_distance) values "+
                      "('%d' , '%d', '%s','%s', '%s','%s','%s', '%d','%d','%d')" % (household_id,
                                                                service_area_id,
                                                                address_street,
                                                                address_city,
                                                                address_state,
                                                                address_zip,
                                                                coordinates,
                                                                road_segment_id,
                                                                road_segment_start_distance,
                                                                road_segment_end_distance)
                      )
          print insertstmt

          cur.execute(insertstmt)
          curr_row += 1
      except:
          pass

    con.commit()
    con.close()

except:
    
    print "I am unable to connect to the database"
    exit()


