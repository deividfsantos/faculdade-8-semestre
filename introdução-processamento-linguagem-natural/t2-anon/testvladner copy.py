from presidio_analyzer import AnalyzerEngine

analyzer = AnalyzerEngine()

results = analyzer.analyze(text="My phone number is 212-555-5555",
                           entities=["PHONE_NUMBER"],
                           language='en')
print(results)