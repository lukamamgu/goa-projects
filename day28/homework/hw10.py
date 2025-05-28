#მოცემული სიაა: ["georgia", "aRMENIA", "greeCE"]. ყველა ელემენტს ჯერ გაუკეთეთ lower, შემდეგ capitalize და დაბეჭდეთ
countries = ["georgia", "aRMENIA", "greeCE"]
capitalized_countries = [country.lower().capitalize() for country in countries]
for country in capitalized_countries:
    print(country)
