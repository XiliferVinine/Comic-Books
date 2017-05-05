

import csv
with open('Doop.html', 'a') as my_file:

	counter = 0
	print("boi")
	for line in my_file:
		print("boyos")
		counter += 1
		if counter == 1:
			print("hello boyos")
			my_file.write("<table>")
			with open('Comic_Book_Database.csv') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					my_file.write("</tr><td>" + row['Comic_Title'] + "</td><td>" + row['Publisher'] + "</td><td>" + row['Issue_Num'] + "</td><td>" + row['Published_Date']+ "</td>")
					#print(row['Comic_Title'], row['Publisher'], row['Issue_Num'], row['Published_Date'])
					print("done?")
					my_file.write("</tr>")
			print("almost done!")
			my_file.write("</table>")
print("done!")