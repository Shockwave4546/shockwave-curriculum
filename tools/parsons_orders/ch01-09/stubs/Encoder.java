// Stub for WPILib Encoder (not in the JDK). Models: reset() zeroes the count; a fresh encoder reads 42.0 so a read-before-reset differs from a read-after-reset.
public class Encoder {
    private double distance = 42.0;
    public Encoder(int a, int b) {}
    public void reset() { distance = 0.0; }
    public double getDistance() { return distance; }
}
