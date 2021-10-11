from parsing import generate_diff2, generate_diff
from stylish import stylish

t = generate_diff2('./tests/fixtures/step6_1.json',
              './tests/fixtures/step6_2.json')
#print(t)
#print(stylish(generate_diff('./tests/fixtures/step6_1.json',
             # './tests/fixtures/step6_2.json')))
print(stylish(generate_diff('./tests/fixtures/step6_base1.yaml',
              './tests/fixtures/step6_base2.yaml')))