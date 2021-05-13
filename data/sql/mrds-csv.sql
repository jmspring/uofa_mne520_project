/*
 * mrds-csv ms sql server schema
 */
USE mrds;

IF OBJECT_ID('dbo.mrds', 'U') IS NOT NULL 
  DROP TABLE dbo.mrds; 

CREATE TABLE mrds (
    dep_id int,
    url varchar(max),
    mrds_id varchar(max),
    mas_id varchar(max),
    site_name varchar(max),
    latitude decimal(14,5),
    longitude decimal(14,5),
    region varchar(max),
    country varchar(max),
    state varchar(max),
    county varchar(max),
    com_type varchar(max),
    commod1 varchar(max),
    commod2 varchar(max),
    commod3 varchar(max),
    oper_type varchar(max),
    dep_type varchar(max),
    prod_size varchar(max),
    dev_stat varchar(max),
    ore varchar(max),
    gangue varchar(max),
    other_matl varchar(max),
    orebody_fm varchar(max),
    work_type varchar(max),
    model varchar(max),
    alteration varchar(max),
    conc_proc varchar(max),
    names varchar(max),
    ore_ctrl varchar(max),
    reporter varchar(max),
    hrock_unit varchar(max),
    hrock_type varchar(max),
    arock_unit varchar(max),
    arock_type varchar(max),
    structure varchar(max),
    tectonic varchar(max),
    ref varchar(max),
    yfp_ba varchar(max),
    yr_fst_prd varchar(max),
    ylp_ba varchar(max),
    yr_lst_prd varchar(max),
    dy_ba varchar(max),
    disc_yr varchar(max),
    prod_yrs varchar(max),
    discr varchar(max)
);
