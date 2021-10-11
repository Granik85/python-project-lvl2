from parsing import generate_diff2, generate_diff

t = generate_diff2('./tests/fixtures/step6_1.json',
              './tests/fixtures/step6_2.json')
#print(t)
generate_diff('./tests/fixtures/step6_1.json',
              './tests/fixtures/step6_2.json')
