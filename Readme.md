Convert Excel to CSV file
=============== 
This project\'s aim consists of a library called **felisaparser** to convert an Excel file to CSV file. It is based on the Pandas Library and it consists of a class made up by just one method: *excel\_to\_csv()*. 
This parser, unlike the Pandas Method, directly dumps the data into a CSV file, without the need of loading a DataFrame and occupy memory.

Installing
==========

``` {.bash}
pip install felisaparser    
```

Usage
=====

``` {.bash}
>>> from felisaparser import parser
>>> parser('Filename.xlsx', ';').excel_to_csv()
```