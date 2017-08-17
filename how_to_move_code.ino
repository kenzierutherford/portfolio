#include <Servo.h>
Servo servoLeft;
Servo servoRight;


void setup() {
  // put your setup code here, to run once:
  servoLeft.attach(12);
  servoRight.attach(11);
 
}

void loop() {
  // put your main code here, to run repeatedly:
 forward();
}
void forward (){
  servoLeft.writeMicroseconds(1700);   //Left wheel is counterclockwise
  servoRight.writeMicroseconds(1300);  //Right wheel is clockwise
}

void turnLeft(){
  servoLeft.writeMicroseconds(1300);  //left wheel clockwise
  servoRight.writeMicroseconds(1300);  //right wheel clockwise
}

void turnRight(){
  servoLeft.writeMicroseconds(1700);  //left wheel is counterclockwise
  servoRight.writeMicroseconds(1700);  //right wheel is clockwise 
}

void backwards(){
  servoLeft.writeMicroseconds(1300);  //left wheel is clockwise
  servoRight.writeMicroseconds(1700);  //right wheel is counterclockwise
}

