from PIL import Image,ImageDraw,ImageFont
from datetime import datetime




class renderImageFromText:
    def setWidthFromLongestLine(self,text):
        lines=text.split("\n")
        old=0
        for line in lines:
            if len(line) > old:
                old=len(line)
        return int(old*(self.fontsize*0.65))

    def setHeightFromLines(self,text):
        lines=text.split("\n")
        print(len(lines))
        f=(self.fontsize*1.333)
        ff=f*len(lines)
        return int(ff)


    def __init__(self,filename,text):
        self.dt=datetime.strftime(datetime.now(),"%m%d%Y")
        self.filename=filename
        self.white=(255,255,255)
        self.black=(0,0,0)
        self.padded=(20,20)
        self.fontsize=16
        self.text=text
        self.width=self.setWidthFromLongestLine(text) 
        self.height=self.setHeightFromLines(text)
        self.size=(self.width,self.height)

        self.image=Image.new("RGB",self.size,self.white)
        self.draw=ImageDraw.Draw(self.image)
        self.font=ImageFont.load_default()
        self.save()

    def save(self):
        try:
            self.draw.text(self.padded,self.text,self.black,font=self.font)
            fname=f"{self.filename}_{self.dt}.jpg"
            print(fname)
            self.image.save(fname)
        except Exception as e:
            print(e,repr(e),str(e))

if __name__ == "__main__":
    t='''image = Image.new("RGBA", (288,432), (255,255,255))
usr_font = ImageFont.truetype("resources/HelveticaNeueLight.ttf", 25)
d_usr = ImageDraw.Draw(image)
d_usr = d_usr.text((105,280), "Travis L.",(0,0,0), font=usr_font)'''
    renderImageFromText("test",t)

