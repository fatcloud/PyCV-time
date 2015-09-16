import processing.net.*;

Server server;
Client client;
String input;
int data[];

void setup () {
  size (400, 400, P2D);
  server = new Server(this, 12345);
 
  img = createImage (width,height,ARGB);
  bufferR = new int[width*height];
  bufferG = new int[width*height];
  bufferB = new int[width*height];
  bufferA = new int[width*height];
 
  source = new CSourceFire(mouseX,mouseY);
}
 
 
void draw () {
 
  background (255);
 
  if (mousePressed == true) {
   source.update(mouseX, mouseY, 1); 
  }
  client = server.available();
  if (client != null) {
    input = client.readString();
    println(input);
    input = input.substring(0, input.indexOf("\n"));
    data = int(split(input, ' '));
    source.update(data[0], data[1], 15);  
  }
  
 
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