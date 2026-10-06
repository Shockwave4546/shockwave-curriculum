package org.wpilib.command3;

import org.wpilib.system.RobotController;

/**
 * Lets exercises run the Commands v3 scheduler without a robot.
 *
 * The scheduler asks the Driver Station which opmode is active, and reads the robot clock; both
 * normally need WPILib's native hardware library. {@link #init()} swaps in a fixed opmode and a
 * clock that only moves when {@link #advance(double)} says so, so runs are deterministic.
 *
 * Our own code. It lives in this package only because OpModeFetcher is package-private.
 */
public final class TestSupport
{
    private static long nanos = 0;

    private TestSupport() {}

    /** Call once, before touching Scheduler. */
    public static void init()
    {
        OpModeFetcher.setFetcher(new OpModeFetcher()
        {
            @Override
            long getOpModeId()
            {
                return 0;
            }

            @Override
            String getOpModeName()
            {
                return "test";
            }
        });
        RobotController.setTimeSource(() -> nanos);
    }

    /** Moves the fake clock forward. */
    public static void advance(double seconds)
    {
        nanos += Math.round(seconds * 1_000_000_000L);
    }
}
