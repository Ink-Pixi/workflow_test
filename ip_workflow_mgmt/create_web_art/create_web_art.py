import win32com.client
import time
import random
import os
from design_info import DesignInfo


class CreateWebArt(object):
    def __init__(self, fileType=None, skus=None):
        super(CreateWebArt, self)
        db = DesignInfo()
        skus = [skus]
        #connect to database.
        db.connect_mysql()
        
        #get the designs
        if not skus:
            skus = db.get_skus()
        
        for sku in skus:
            #Make .pngs.
            if fileType == 'png':
                MakePng(sku)
            elif fileType == 'static':
                #Make static images.
                MakeStatic(sku)
            else:
                MakePng(sku)
                MakeStatic(sku)

class MakeStatic(object):
    def __init__(self, sku=None):
        super(MakeStatic, self).__init__()
        
        di = DesignInfo()

        #this is where the garment selection logic should probably go.
        
        self.cnt = 1
#         for sku in skus:
#             designInfo = di.get_design_info(sku) 
#             hatColor = di.get_hat_color(sku)
#             self.make_static_images(sku, designInfo, hatColor)
        if sku:
            designInfo = di.get_design_info(sku) 
            hatColor = di.get_hat_color(sku)
            self.make_static_images(sku, designInfo, hatColor)            
        
    def make_static_images(self, sku, designInfo, hatColor, garments=None, var1type=None, var2type=None, var1case=None, var2case=None, v1CustomName=0, v2CustomName=0, isPosessive=0):
        di = DesignInfo()
        
        vnum = designInfo[0]
        isHat = 0
        if hatColor:
            isHat = 1
        color = designInfo[1]
        v1envelope = designInfo[4]
        v2envelope = designInfo[5]
        
        aiApp = win32com.client.Dispatch("Illustrator.Application")
        
        time.sleep(5)
        aiApp.Application.UserInteractionLevel = -1
        
        #this should probably go above in the __init__ if this goes gui
        
        design_y_fix_big = 0
        design_x_fix_big = 0
        
            # If there is a hat in this design, open the corresponding hat AI file
        if isHat == 1:
            docHat = aiApp.Open(r"\\WAMPSERVER\xampp\art_files\aiFiles\\" + sku + "-Hat.ai")
         
        aiApp.Open(r"\\WAMPSERVER\xampp\art_files\aiFiles\\" + sku + ".ai")
        
        origDocument = aiApp.Application.ActiveDocument
        # add new layer as a place to house py the grouped items
        nl = origDocument.Layers.Add()
        nl.Name = "zoom"
        # clear the distress flag in case the next design artwork has none.
        distress = 0
        for i in range(0, origDocument.Layers[1].GroupItems.Count):
            newGroup = nl.GroupItems.Add()
            newGroup.Name = origDocument.Layers[1].GroupItems[i].Name
            for z in range(0, origDocument.Layers[1].GroupItems[i].PageItems.Count):
                origDocument.Layers[1].GroupItems[i].PageItems[z].Duplicate(newGroup, 2)
                # check to see if there is a distress layer. if so, set distress var to 1.
                for d in range(0, origDocument.Layers[1].GroupItems.Count):
                    if origDocument.Layers[1].GroupItems[d].Name == "distress":
                        distress = 1
        # set the new distress layer's opacity to the original distress layer setting
        if distress == 1:
            nl.GroupItems["distress"].Opacity = origDocument.Layers[1].GroupItems["distress"].Opacity

      
        # open the web_art.ai template
        doc = aiApp.Open(r"\\WAMPSERVER\xampp\art_files\Blanks_375x500.ai")

        # define and add the layer/sublayers we'll be duplicating to.
        masterArtLayer = doc.Layers("dynamic art")
        masterArtLayer.Visible = True
        desLayer = masterArtLayer.Layers.Add()
        desLayer.Name = sku
        zoomLayer = desLayer.Layers.Add()
        zoomLayer.Name = "zoom"
        copyGroup = zoomLayer.GroupItems.Add()
        copyGroup.Name = "group"
        # duplicate the grouped items from the other document to this document
        for gi in range(0, origDocument.Layers["zoom"].PageItems.Count):
            origDocument.Layers["zoom"].PageItems[gi].Duplicate(zoomLayer)
            zoomLayer.PageItems[0].Duplicate(copyGroup)
            zoomLayer.PageItems[0].Delete()
        # if there is a hat with this design, duplicate the artwork from the hat AI file to our new layer
        if isHat == 1:
            hatGroup = zoomLayer.GroupItems.Add()
            hatGroup.Name = "hatgroup"
            hatArtName = "hat"
            docHat.Layers[hatArtName].Visible = True
            docHat.Layers[hatArtName].PageItems[0].Duplicate(zoomLayer)
            zoomLayer.PageItems[0].Name = "hatArt"
            zoomLayer.PageItems[0].Duplicate(hatGroup)
            zoomLayer.PageItems[0].Delete()
            zoomLayer.GroupItems["hatgroup"].PageItems["hatArt"].hidden = True

        # delete the newly created layers from the original documents since we don't need them now.
        origDocument.Layers["zoom"].Delete()


        
        var_1_type = 'general' if not var1type else var1type
        var_2_type = 'places' if not var2type else var2type
        v1_case = 'Upper w// Mc' if not var1case else var1case
        v2_case = 'Upper w// Mc' if not var2case else var2case



        
        # get name data based on combobox selection
        names = di.get_names(var_1_type, var_2_type)
        v1names = list()
        for name in names:
            v1names.append(name[0])

        if vnum == 2:  # If there are 2 variables in the design, get the 2nd variable name data based on combobox selection
            names = di.get_names(var_1_type, var_2_type)
            v2names = []
            for name in names:
                v2names.append(name[0])
                

        #********************************************************************** Y LOOP ****************************************************************
        # Check to see if any checkboxes are checked so we know whether or not to run only checked items or run the whole batch
        #keep this here for now
        if not garments:
            garmList = designInfo[3].split(',')
        else:
            garmList = []
            for k in garments:
                garmList.append(k)            

        # loop through each garment available for this color (x)
        for y in garmList:
            masterArtLayer = doc.Layers("dynamic art")
            designLayer = masterArtLayer.Layers(sku)

            zoomLayer = designLayer.Layers("zoom")
            groupLayer = zoomLayer.GroupItems("group")
            if isHat == 1:
                hatgroupLayer = zoomLayer.GroupItems("hatgroup")
            
            #why are these here?
#             v1textLayer = groupLayer.GroupItems["var1"].TextFrames[0]
#             artLayer = groupLayer.PageItems("design")
            
            #why is this here?
#             if vnum == 2:
#                 v2textLayer = groupLayer.GroupItems["var2"].TextFrames[0]
#                     
                
            # Grab a random name from the db or use the user provided name
            if y == "hat":
                v1RndName = random.choice(v1names)   
            elif v1CustomName == 1 and self.cust[y].get() != '':
                v1RndName = self.cust[y].get()
            else:
                v1RndName = random.choice(v1names)  
            # If 'Make Possessive' was checked, ad 's to the end of name (except for German names)
            if isPosessive == 1:
                if v1RndName[-1:].lower() != "s" and var_1_type != "german":
                    v1RndName = v1RndName + "'s"                     
            v1RndName = self.word_case_format(v1RndName, v1_case)

            
            if vnum == 2:  # if this is a 2 variable design, grab a second random name/place etc.
                if y == "hat":
                    v2RndName = random.choice(v2names)
                elif v2CustomName == 1 and self.cust2[y].get() != '':
                    v2RndName = self.cust2[y].get()
                else:
                    v2RndName = random.choice(v2names)    
                v2RndName = self.word_case_format(v2RndName, v2_case)


            doc.Layers["bg"].Visible = True
            doc.Layers["bg"].PageItems[0].hidden = False
            
            if y == "collage":  
                doc.Layers["tshirt"].Visible = True  # Make garment layer visible
                if isHat == 1:
                    doc.Layers["hat_collage"].Visible = True
                doc.Layers["tshirt"].Layers[color].Visible = True  # Make specific colored garment visible
                doc.Layers["tshirt"].Layers[color].PageItems[0].hidden = False
                if isHat == 1:
                    doc.Layers["hat_collage"].Layers[hatColor].Visible = True  # Make specific colored garment visible
                    doc.Layers["hat_collage"].Layers[hatColor].PageItems[0].hidden = False
            elif y == "hat":
                doc.Layers[y].Visible = True
                doc.Layers[y].Layers[hatColor].Visible = True
                doc.Layers[y].Layers[hatColor].PageItems[0].hidden = False
            elif y == "apron":
                print('need template.')
            else:
                doc.Layers[y].Visible = True
                doc.Layers[y].Layers[color].Visible = True
                doc.Layers[y].Layers[color].PageItems[0].hidden = False



                
            masterArtLayer.Visible = True  # Make master art layer visible
            designLayer.Visible = True  # Turn on specific design layer
            zoomLayer.Visible = True


                
            # Since we're working from the original imported artwork,
            # we'll add a new layer to copy it to, then modify it based on which image we're making.        
            # This layer will be added then deleted each iteration of the loop.
            new_layer = designLayer.Layers.Add()    
            new_layer.Name = "zoom_copy"

            zoomLayer.Visible = True
            groupLayer.Duplicate(new_layer)
            if isHat == 1:
                hatgroupLayer.Duplicate(new_layer)
            zoomLayer.Visible = False
                
            new_layer.Visible = True

            #newzoomLayer = designLayer.Layers("zoom_copy")
            newgroupLayer = new_layer.GroupItems("group")
            if isHat == 1:
                newhatgroupLayer = new_layer.GroupItems("hatgroup")
            newv1textLayer = newgroupLayer.GroupItems["var1"]
            if vnum == 2:
                newv2textLayer = newgroupLayer.GroupItems["var2"]
            newartLayer = newgroupLayer.GroupItems("design")
            if distress == 1:
                newdistressLayer = newgroupLayer.PageItems("distress")

            # resize image and set XY coordinates to place the various artwork where it needs to be.
            if y == "zoom_bg":
                newgroupLayer.Resize(45, 45, True, True, True, True, 45)
                newgroupLayer.Top = doc.Layers["bg"].PageItems[0].Top - ((doc.Layers["bg"].PageItems[0].Height / 2) + (newgroupLayer.Height / 2)) + design_y_fix_big
                newgroupLayer.Left = (375 / 2) - (newgroupLayer.Width / 2) + design_x_fix_big
            elif y == "onesie":
                newgroupLayer.Resize(30, 30, True, True, True, True, 30)
                newgroupLayer.Top = -130 - design_y_fix_big
                newgroupLayer.Left = (375 / 2) - ((newgroupLayer.Width / 2) + (design_x_fix_big)) -35
            elif y == "hoodie":
                newgroupLayer.Resize(30, 30, True, True, True, True, 30)
                newgroupLayer.Top = -120 - design_y_fix_big
                newgroupLayer.Left = ((375 / 2) - (newgroupLayer.Width / 2)) - 30 - design_x_fix_big  
            elif y == "hat":
                newgroupLayer.hidden = True
                newgroupLayer.Selected = False                         
                newhatgroupLayer.PageItems["hatArt"].hidden = False
                newhatgroupLayer.PageItems["hatArt"].Selected = True
                newhatgroupLayer.Resize(19, 19, True, True, True, True, 19)
                                                 
                newhatgroupLayer.Top = ((newhatgroupLayer.Height / 2) - 200) - design_y_fix_big
                newhatgroupLayer.Left = (375 / 2) - (newhatgroupLayer.Width / 2) -2 - design_x_fix_big                   
            elif y == "collage":
                # first make the hat image
                newgroupLayer.hidden = True
                newgroupLayer.Selected = False
                if isHat == 1:
                    newhatgroupLayer.PageItems["hatArt"].hidden = False
                    newhatgroupLayer.PageItems["hatArt"].Selected = True
                    newhatgroupLayer.Resize(10, 10, True, True, True, True, 10)
                    hat_y_box_small_fix = int()
                    if self.hat_y_adj.get() == "":
                        hat_y_box_small_fix = 0
                    else:
                        hat_y_box_small_fix = int(self.hat_y_adj.get())
                    newhatgroupLayer.Top = (340 + hat_y_box_small_fix)
                    newhatgroupLayer.Left = 375 - (newhatgroupLayer.Width / 2)
                    newhatgroupLayer.hidden = True
                # now make the shirt image
                doc.Layers["tshirt"].Layers[color].Visible = True
                doc.Layers["tshirt"].Visible = True
                newgroupLayer.hidden = False
                newgroupLayer.Selected = True
                newgroupLayer.Resize(20, 20, True, True, True, True, 20)
                newgroupLayer.Top = 469 + design_y_fix_big
                newgroupLayer.Left = 533 - (newgroupLayer.Width / 2) + design_x_fix_big
                
            else:
                newgroupLayer.Resize(30, 30, True, True, True, True, 30)
                newgroupLayer.Top = -138 -design_y_fix_big
                # newgroupLayer.Left = 245 - (newgroupLayer.Width/2) + design_x_fix_big
                newgroupLayer.Left = ((375 / 2) - (newgroupLayer.Width / 2)) - 30 -design_y_fix_big

            #if y != "hat":
            if y!= "hat":
                # make a new layer inside this layer to house the var1 text
                # THE TEXTFRAME NEEDS TO BE SELECTED BEFORE THE CONTENTS ARE
                #CHANGED SO THE FONT STYLE FOLLOWS THROUGH!!!!!!
                newv1textLayer.TextFrames[0].Selected = True

                newv1textLayer.TextFrames[0].Contents = v1RndName
                #newv1textLayer.TextFrames[0].Contents = 'Ted'
                newv1textLayer.Selected = True
                newartLayer.Selected = False
                if distress == 1:
                    newdistressLayer.Selected = False
                if vnum == 2:
                    newv2textLayer.hidden = True
                
                # run action in illustrator to create envelope if needed
                if v1envelope != 2:
                    aiApp.DoScript('Create Envelope', 'Default Actions')
                    while(aiApp.ActionIsRunning):
                        time.sleep(100)
                
                
                # if there are 2 variables, create envelope for var 2 as well.
                # FOR SUB LAYER ITEMS VISIBILITY, USE PageItems and the attribute 'hidden'
                if vnum == 2:
                    newv2textLayer.hidden = False
                    newv1textLayer.hidden = True
                    newv2textLayer.TextFrames[0].Selected = True
                    newv2textLayer.TextFrames[0].Contents = v2RndName
                    newv2textLayer.Selected = True
                    newartLayer.Selected = False                    

                    # run action in illustrator to create var 2 envelope if needed
                    if v2envelope == 1:
                        aiApp.DoScript('Create Envelope', 'Default Actions')
                        while(aiApp.ActionIsRunning):
                            time.sleep(100)
                    newv1textLayer.hidden = False
            
            def SEOify(color):
                seo = color.strip()
                seo = seo.lower()
                seo = seo.replace(" - ", "-")
                seo = seo.replace(" ", "-")
                seo = seo.replace("'", "")
                seo = seo.replace("/", "-")
            
                return seo
            #get the descriptive design name for saving.
            designName = SEOify(designInfo[6])
            # Adjust settings for different types of output
            if y == "zoom_bg":
                doc.Layers[y].Layers["stroke"].Visible = True
                designColor = SEOify(color)
                imageSaveLocal = os.path.abspath(r"\\wampserver\test_images\david\\" + designColor + "-" + designName + "-zoom.jpg")
            elif y == "hat":
                designColor = SEOify(hatColor)
                imageSaveLocal = os.path.abspath(r"\\wampserver\test_images\david\\"+ designColor + "-" + designName +"-personalized-embroidered-hat-sm.jpg")
            else:
                designColor = SEOify(color)
                imageSaveLocal = os.path.abspath(r"\\wampserver\test_images\david\\"+ designColor + "-" + designName + '-personalized-' + y + "-sm.jpg")
                


            jpegExportOptions = win32com.client.Dispatch("Illustrator.ExportOptionsJPEG")
            jpegExportOptions.AntiAliasing = False
            jpegExportOptions.ArtBoardClipping = True
            jpegExportOptions.QualitySetting = 80
            doc.Export (imageSaveLocal, 1, jpegExportOptions)

            if y == "zoom_bg":
                doc.Layers[y].Layers["stroke"].Visible = False
                doc.Layers[y].Layers[color].Visible = False
                doc.Layers[y].Visible = False
            elif y == "collage":
                doc.Layers["tshirt"].Layers[color].Visible = False
                if isHat == 1:
                    doc.Layers["hat_collage"].Layers[hatColor].Visible = False
                    doc.Layers["hat_collage"].Visible = False
                doc.Layers["tshirt"].Visible = False
            elif y == "hat":
                doc.Layers["hat"].Layers[hatColor].Visible = False
                doc.Layers["hat"].Visible = False
            elif y == 'apron':
                print('need template images')
            else:
                doc.Layers[y].Layers[color].Visible = False
                doc.Layers[y].Visible = False

            new_layer.Delete()
            zoomLayer.Visible = False
            designLayer.Visible = False
            doc.Layers["bg"].Visible = False
            
        
        designLayer.Visible = True
        designLayer.Delete()
        masterArtLayer.Visible = False


        # Close the web_art.ai template
        #origDocument.Close(2)
        #doc.Close(2)
        if isHat == 1:
            docHat.Close(2)   
        # popup a dialog and ask if the user wants to continue on with making the small images too....if not, close the Illustrator documents
#             result = messagebox.askyesno('Small Images', 'Do you want to make the small images too?')
#             if result == True:
#                 self.make_small_images()


            # close the open documents
         
        origDocument.Close(2)
        
    def word_case_format(self, n, c):  # Function to change names to specific case -- n is the name, c is case type
        """Change names to selected case type - 1.upper/2.proper/3.upper with Mc exception/4.lower """
        if c == 1:  # UPPERCASE
            n = n.upper()
        elif c == 2:  # Propercase
            # if there are multiple words, split them into a list and capitalize each word
            nList = n.split()
            k = list()
            if len(nList) > 1:
                # loop through words and capitalize each of them
                for i in nList:
                    k.append(i.capitalize())
                # convert list back into string with spaces in between
                n = " ".join(k)
            else:    
                n = n.capitalize()
        elif c == 3:  # McUPPERCASE
            first_n = n[:2]  # first two characters
            last_n = n[2:]  # from 3rd character to end of string
            if first_n.lower() == "mc" or first_n.lower() == "o'":
                n = first_n.capitalize() + last_n.upper()
            else:
                n = n.upper()
        elif c == 4:  # lowercase
            n = n.lower()
        else:
            n = n

        return n        
            

class MakePng(object):
    def __init__(self, sku=None):
        super(MakePng, self).__init__()
        di = DesignInfo()
        self.cnt = 1
        
        if sku:
            designInfo = di.get_design_info(sku) 
            hatColor = di.get_hat_color(sku)
                
            self.make_png_images(sku, designInfo, hatColor)

    def make_png_images(self, sku, designInfo, hatColor):
        #retrieve amount of variables in design.
        vnum = designInfo[0]
        isHat = 0
        if hatColor:
            isHat = 1
        hasOverlay = designInfo[2]

        def save_png():
            pngExportOptions = win32com.client.Dispatch("Illustrator.ExportOptionsPNG24")
            pngExportOptions.artBoardClipping = True            
            doc.Export (imageSaveLocal, 5, pngExportOptions)  
                   
        aiApp = win32com.client.Dispatch("Illustrator.Application")
        
        time.sleep(5)
        aiApp.Application.UserInteractionLevel = -1
        
        for artSize in ["750", "375"]:
            # If there is a hat in this design, open the corresponding hat AI file
            if isHat == 1:
                docHat = aiApp.Open(r"\\wampserver\xampp\art_files\aiFiles\\"+sku+"-HATS-NONAME.ai")
             
            aiApp.Open(r"\\WAMPSERVER\xampp\art_files\aiFiles\\"+sku+".ai")
            
            origDocument = aiApp.Application.ActiveDocument
            # add new layer as a place to house py the grouped items
            nl = origDocument.Layers.Add()
            nl.Name = "zoom"
            for i in range(0, origDocument.Layers[1].GroupItems.Count):
                newGroup = nl.GroupItems.Add()
                newGroup.Name = origDocument.Layers[1].GroupItems[i].Name
                for z in range(0, origDocument.Layers[1].GroupItems[i].PageItems.Count):
                    origDocument.Layers[1].GroupItems[i].PageItems[z].Duplicate(newGroup, 2)
                    # check to see if there is a distress layer. if so, set distress var to 1.
#                     for d in range(0, origDocument.Layers[1].GroupItems.Count):
#                         if origDocument.Layers[1].GroupItems[d].Name == "distress":
#                             distress = 1
            #set the new distress layer's opacity to the original distress layer setting
            if hasOverlay == 1:
                nl.GroupItems["distress"].Opacity = origDocument.Layers[1].GroupItems["distress"].Opacity

          
            # open the web_art.ai template
            doc = aiApp.Open(r"\\WAMPSERVER\xampp\art_files\png_template_" + artSize + ".ai")

            # define and add the layer/sublayers we'll be duplicating to.
            
            #Open the template and set layers
            masterArtLayer = doc.Layers("dynamic art")
            masterArtLayer.Visible = True
            #Add a new sub-layer to the template
            desLayer = masterArtLayer.Layers.Add()
            #Name new template the name of the design we are currently working on ex. A101
            desLayer.Name = sku
            #Add another layer...
            zoomLayer = desLayer.Layers.Add()
            #Call this new layer zoom
            zoomLayer.Name = "zoom"
            #add a group to this layer
            copyGroup = zoomLayer.GroupItems.Add()
            #call this group group.
            copyGroup.Name = "group"
            
            #for py the items in the zoom layer of the art template we want to copy to the 
            #web template and delete from the art template
            for gi in range(0, origDocument.Layers["zoom"].PageItems.Count):
                #create zoom layer in web template to hold copied layer
                origDocument.Layers["zoom"].PageItems[gi].Duplicate(zoomLayer)
                #copy layer and move it to web template.
                zoomLayer.PageItems[0].Duplicate(copyGroup)
                #delete the layer just created from the art template so it doesn't get saved to the file.
                zoomLayer.PageItems[0].Delete()  
                
            # if there is a hat with this design, duplicate the artwork from the hat AI file to our new layer
            # hide it and call it hatgroup.
            if isHat == 1:
                #create new layer in web template.
                hatGroup = zoomLayer.GroupItems.Add()
                #name the group "hatgroup"
                hatGroup.Name = "hatgroup"
                hatArtName = "hat"
                #turn on hat desing in art template?
                docHat.Layers[hatArtName].Visible = True
                #copy the the layers from the art template
                docHat.Layers[hatArtName].PageItems[0].Duplicate(zoomLayer)
                zoomLayer.PageItems[0].Name = "hatArt"
                #copy the layers and groups to the web template.
                zoomLayer.PageItems[0].Duplicate(hatGroup)
                #delete the newly created layer in the art template.
                zoomLayer.PageItems[0].Delete()
                #Then hide the hat layer so we can run the shirt art first.
                zoomLayer.GroupItems["hatgroup"].PageItems["hatArt"].hidden = True  
                
            # delete the newly created layers from the original documents since we don't need them now.
            origDocument.Layers["zoom"].Delete()        

            masterArtLayer = doc.Layers("dynamic art")
            designLayer = masterArtLayer.Layers(sku)

            zoomLayer = designLayer.Layers("zoom")
            groupLayer = zoomLayer.GroupItems("group")
            if isHat == 1:
                hatgroupLayer = zoomLayer.GroupItems("hatgroup")
                
            masterArtLayer.Visible = True  # Make master art layer visible
            designLayer.Visible = True  # Turn on specific design layer
            zoomLayer.Visible = True
            
            # Since we're working from the original imported artwork,
            # we'll add a new layer to copy it to, then modify it based on which image we're making.        
            # This layer will be added then deleted each iteration of the loop.
            new_layer = designLayer.Layers.Add()    
            new_layer.Name = "zoom_copy"

            zoomLayer.Visible = True
            groupLayer.Duplicate(new_layer)
            if isHat == 1:
                hatgroupLayer.Duplicate(new_layer)
            zoomLayer.Visible = False
                
            new_layer.Visible = True

            newzoomLayer = designLayer.Layers("zoom_copy")
            newgroupLayer = new_layer.GroupItems("group")
            if isHat == 1:
                newhatgroupLayer = new_layer.GroupItems("hatgroup")
            #newv1textLayer = newgroupLayer.GroupItems["var1"]
            #if vnum == 2:
                #newv2textLayer = newgroupLayer.GroupItems["var2"]
            #newartLayer = newgroupLayer.GroupItems("design")
            #if distress == 1:
                #newdistressLayer = newgroupLayer.PageItems("distress")      
            
            if artSize == "750":
                newgroupLayer.Resize(60, 60, True, True, True, True, 60)
            else:
                newgroupLayer.Resize(30, 30, True, True, True, True, 30)
            newgroupLayer.Top = (newgroupLayer.Height / 2) -250
            newgroupLayer.Left = ((int(artSize) / 2) - (newgroupLayer.Width / 2)) 
           
            #turn off var1 text..
            newgroupLayer.PageItems("var1").hidden = True
            newgroupLayer.PageItems("distress").hidden = True
            #if there is a second varible we want to turn that off too..
            if vnum == 2:
                newgroupLayer.PageItems("var2").hidden = True 
            #set iage save pathh
            imageSaveLocal = os.path.abspath(r"\\wampserver\test_images\david\\" + sku + "_design_x"+ artSize +".png")
            #save image     
            save_png()
            
            if hasOverlay == 1:
                newgroupLayer.PageItems("distress").hidden = False
                newgroupLayer.PageItems("design").hidden = True
                
                imageSaveLocal = os.path.abspath(r"\\wampserver\test_images\david\\" + sku + "_overlay_design_x"+artSize+".png")
                
                save_png()
 
            if isHat == 1:
                #show the hat artwork
                newhatgroupLayer.PageItems("hatArt").hidden = False
                #hide the standard artwork
                newzoomLayer.PageItems("group").hidden = True
                
                if artSize == "750":
                    newhatgroupLayer.Resize(32, 32, True, True, True, True, 32)
                else:
                    newhatgroupLayer.Resize(30, 30, True, True, True, True, 30)
                    
                newhatgroupLayer.Top = (newhatgroupLayer.Height / 2) - 250
                newhatgroupLayer.Left = ((int(artSize) / 2) - (newhatgroupLayer.Width / 2))                 
                    
                #set image path
                imageSaveLocal = os.path.abspath(r"\\wampserver\test_images\david\\" + sku + "_design_hat_x"+artSize+".png")
                #save the image
                save_png()
                
            
            new_layer.Delete()
            zoomLayer.Visible = False
            designLayer.Visible = False
              
            designLayer.Visible = True
            designLayer.Delete()
            masterArtLayer.Visible = False
    
    
            # close the open documents
            if isHat == 1:
                docHat.Close(2)
            doc.Close(2)
            origDocument.Close(2)  
            
            self.cnt += 1
            if self.cnt == 25:
                print('Restarting Adobe Illustrator')
                
                aiApp.Quit()

                aiApp = win32com.client.Dispatch("Illustrator.Application")
                time.sleep(5)
                aiApp.Application.UserInteractionLevel = -1
                
                self.cnt = 1      
                

                
if __name__ == '__main__':            
    cwa = CreateWebArt()