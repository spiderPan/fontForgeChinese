import os,fontforge;
imgsPath = "D:/phpstudy/www/img";
imgs = os.listdir(imgsPath);
font = fontforge.activeFont();
i = 0;
for index in xrange(len(imgs)): 
 fontforge.logWarning("index:"+str(index));imgName = imgs[index][:-4];fontforge.logWarning("imgName:"+imgName)
 glyph=font.createChar(int(imgName,16),"uni"+imgName);
 layer=glyph.foreground;
 if layer.isEmpty():
   try:        
                 glyph.importOutlines(imgsPath+"/"+imgs[index]);
   except:  
                 fontforge.logWarning(str(index)+"/"+str(len(imgs))+":"+imgsPath+"/"+imgs[index]+"is error");
                 continue;
   else:
                 glyph.autoTrace();glyph.simplify();glyph.activeLayer=0;glyph.clear();i=i+1;
                 fontforge.logWarning(str(index)+"/"+str(len(imgs))+":"+imgsPath+"/"+imgs[index]+"is OK"+str(i))
                 if i==50:
                    break;
 else:
                 continue;
  