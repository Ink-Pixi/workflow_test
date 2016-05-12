import mysql.connector
from contextlib import closing


class DesignInfo(object):
    def __init__(self):
        super(DesignInfo, self).__init__()
                
    def connect_mysql_wampserver(self):
        conn = mysql.connector.connect(user = 'AI_APP', password = 'rowsby01', host = 'wampserver', database = 'xaotees-inkpixi', raise_on_warnings = True)
        
        return conn     
    
    def connect_mysql_inkpixi(self):
        conn = mysql.connector.connect(user = 'root', password = '7701esm', host = 'inkpixi', database = 'inkpixi', raise_on_warnings = True)
        
        return conn   
    
    def get_skus(self):
        conn = self.connect_mysql_wampserver()
        cur = conn.cursor()
        with closing(cur) as db:
            #db.execute('select sku_code from designs where visible = 1 order by right(sku_code, 3), sku_code')
            #db.execute('select sku_code from designs where visible = 1 and right(sku_code, 3) > 240 order by right(sku_code, 3), sku_code')
            db.execute("""SELECT 
                                d.sku_code
                            FROM 
                                packages p
                            LEFT JOIN 
                                designs d on p.design_id = d.id and p.garment_styles_age_id IN (5, 19)
                            WHERE
                                d.visible = 1
                            AND
                                sku_code IN ('A101', 'A223')
                            GROUP BY 
                                d.sku_code
                            ORDER BY
                                RIGHT(sku_code, 3)""")
            ds = db.fetchall()
        lsSkus = []
        for i in ds:
            lsSkus.append(i[0])
        
        return lsSkus

    def get_art_name_types(self):
        conn = self.connect_mysql_wampserver()
        cur = conn.cursor()
        with closing(cur) as db:
            db.execute('select name_types from art_name_types')
            ds = db.fetchall()
        
        lsNames = []
        for row in ds:
            lsNames.append(row[0])
        
        return lsNames
    
    def get_hat_color(self, sku):
        conn = self.connect_mysql_wampserver()
        cur = conn.cursor()
        with closing(cur) as db:
            db.execute("""SELECT
                            c.name
                        FROM 
                            packages p
                        LEFT JOIN 
                            designs d on p.design_id = d.id and (p.garment_styles_age_id = 5 or p.garment_styles_age_id = 19)
                        LEFT JOIN 
                            colors c on c.id = p.color_id
                        WHERE 
                            d.sku_code = '"""+sku+"""'
                        GROUP BY 
                            d.id""")
            ds = db.fetchone()
            
            return ds[0]        
        
    def get_design_info(self, sku):
        conn = self.connect_mysql_wampserver()
        cur = conn.cursor()
        
        with closing(cur) as db:
            db.execute("""
                        SELECT 
                            d.variable_count,
                            c.name,
                            d.overlay,
                            c.garments,
                            d.var_1_resize,
                            d.var_2_resize,
                            d.name                            
                        FROM 
                            packages p
                        LEFT JOIN 
                            designs d on p.design_id = d.id and p.garment_styles_age_id = 1
                        LEFT JOIN 
                            colors c on c.id = p.color_id
                        WHERE 
                            d.sku_code = '"""+sku+"""'
                        GROUP BY 
                            d.id""")
            ds = db.fetchone()
        
        return ds        
    
    def get_names(self, var1Type, var2Type):
        conn = self.connect_mysql_wampserver()
        cur = conn.cursor()
        
        with closing(cur) as db:
            db.execute("SELECT distinct(" + var1Type + ") FROM `art_names` where " + var2Type + " is not null")
            ds = db.fetchall()
            
        return ds
    
    def get_invetories_names(self, sku):
        conn = self.connect_mysql_inkpixi()
        cur = conn.cursor()
        
        with closing(cur) as db:
            db.execute("""SELECT
                                inventories_name 
                            FROM
                                inventories
                            WHERE 
                                LEFT(inventories_code, 4) = '"""+sku+"""';""")
            ds = db.fetchall()
            
            return ds