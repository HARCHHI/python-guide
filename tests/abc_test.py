from samples.abcS import Animal


class HealthyDog(Animal):
    def run(self) -> int:
        return 1

    def sleep(self) -> int:
        return 1


class TestAbcFeatures:
    def test_implement1(self):
        a = HealthyDog()
        a.run()
        a.sleep()
        assert True
