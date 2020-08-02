import xlwt
import xlrd


 
def readStudents(loc):
    file = loc.split('\\')[-1]
    file = file.split('.')[0]
    students = []
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)
    
    rows = sheet.nrows
      
    for i in range(rows): 
        students.append(sheet.cell_value(i, 0))
    wb.release_resources()
    
    return rows,students,file
    

def writeAttendance(rows,attendance,students,file):
    workbook = xlwt.Workbook()   
    sheet = workbook.add_sheet("Attendance") 
      
    for i in range(1,rows+1):
        sheet.write(i, 0, students[i-1])
        
    for i in range(1,rows+1):
        for j in range(len(attendance)):
            if attendance[j] == students[i-1]:
                sheet.write(i, 1, 1)
     
    workbook.save(file+'.xls')
    
    

