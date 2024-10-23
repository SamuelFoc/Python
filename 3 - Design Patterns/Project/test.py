import unittest

# Discover and run tests in the Musicer.tests module
if __name__ == "__main__":
    # Ensure test methods start with "test"
    unittest.defaultTestLoader.testMethodPrefix = "test"

    # Run the test suites from the different test modules
    test_modules = [
        'Musicer.tests.test_playback',
        'Musicer.tests.test_playlist',
        'Musicer.tests.test_subscription',
        'Musicer.tests.test_commands',
        'Musicer.tests.test_global',
    ]

    # Load the tests from the modules and run them
    for module in test_modules:
        suite = unittest.defaultTestLoader.loadTestsFromName(module)
        unittest.TextTestRunner().run(suite)