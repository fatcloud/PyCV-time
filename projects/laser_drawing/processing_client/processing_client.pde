import processing.net.*; 
Client myClient; 
int dataIn; 
 
void setup() { 
  size(400, 400); 
  // Connect to the local machine at port 12345.
  // This example will not run if you haven't
  // previously started a server on this port.
  myClient = new Client(this, "127.0.0.1", 12345); 
} 
 
void mouseMoved() {
  myClient.write(mouseX+" "+mouseY+"\n");
}

void draw() { 
  if (myClient.available() > 0) { 
    println("connected");
    dataIn = myClient.read(); 
    println(mouseX + " " + mouseY);
  } 
  background(dataIn); 
} 