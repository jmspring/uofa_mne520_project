USE mrds;

BULK INSERT mrds
    from '/tmp/mrds.csv'
    with
(
    format='csv',
    fieldquote = '"',
    firstrow=2,
    FIELDTERMINATOR=',',
    ROWTERMINATOR='\n',
    TABLOCK,
    ERRORFILE='/tmp/errorfile.csv'
);