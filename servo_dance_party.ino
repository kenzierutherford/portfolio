#include <Servo.h>

Servo servoLeft;
Servo servoRight;

void setup() {
  servoLeft.attach(13);
  servoRight.attach(12);

  pinMode(11, OUTPUT);
}

/*
int main(){
  freqout(11, 1000, 3000);                     
}
*/
void loop() {
 servoLeft.writeMicroseconds(2160);
 servoRight.writeMicroseconds(2160);
  delay(10);
 servoLeft.writeMicroseconds(1010);
 servoRight.writeMicroseconds(-1010);

 servoLeft.writeMicroseconds(-510);
 servoRight.writeMicroseconds(510);

 servoLeft.writeMicroseconds(310);
 servoRight.writeMicroseconds(-310);

 servoLeft.writeMicroseconds(-4000);
 servoRight.writeMicroseconds(4000);

 tone(11, 2028);
 delay(300);
 noTone(11);
 delay(10);

 tone(11, 3400);
 delay(300);
 noTone(11);
 delay(10);

 tone(11, 2028);
 delay(300);
 noTone(11);
 delay(10);

 tone(11, 3400);
 delay(300);
 noTone(11);
 delay(10);

 tone(11, 2028);
 delay(300);
 noTone(11);
 delay(10);

 tone(11, 3400);
 delay(600);
 noTone(11);
 delay(10);

  tone(11, 3830);
 delay(1000);
 noTone(11);
 delay(10);

 tone(11, 3400);
 delay(500);
 noTone(11);
 delay(10);

 tone(11, 3830);
 delay(300);
 noTone(11);
 delay(10);

  tone(11, 3400);
 delay(500);
 noTone(11);
 delay(500);


}





