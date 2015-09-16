void setup () {
  size (400,400,P2D);
 
  img = createImage (width,height,ARGB);
  bufferR = new int[width*height];
  bufferG = new int[width*height];
  bufferB = new int[width*height];
  bufferA = new int[width*height];
 
  source = new CSourceFire(mouseX,mouseY);
}
 
 
void draw () {
 
  background (255);
 
  source.update(mouseX,mouseY,15);
 
  cleanBorders(bufferA);
  cleanBorders(bufferR);
  cleanBorders(bufferG);
  cleanBorders(bufferB);
 
  fastBlur(bufferR);
  fastBlur(bufferG);
  fastBlur(bufferB);
 
  fastBlur(bufferA);
  fastBlur(bufferA);
  fastBigBlur(bufferA);
 
  source.getImage(img);
  image(img,0,0);
}