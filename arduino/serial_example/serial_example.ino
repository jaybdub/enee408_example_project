#define BAUD_RATE 9600

void setMotorSpeeds(int leftSpeed, int rightSpeed)
{
    // Display new speed
    Serial.print("Left: ");
    Serial.print(leftSpeed);
    Serial.print("Right: ");
    Serial.print(rightSpeed);
    Serial.print("\n");

    // Set speed by controlling pins
    // TODO: Add motor control code
}

void setup()
{
    Serial.begin(BAUD_RATE);
}

void loop()
{
    // TODO: Read serial line and parse
    // TODO: setMotorSpeeds(leftSpeed, rightSpeed);
}