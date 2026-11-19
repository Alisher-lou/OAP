def read_numbers(prompt, min_count=0):
    """Бір жолдағы бүтін сандарды тізімге оқиды. Қате болса, қайта сұрайды."""
    while True:
        text = input(prompt)
        try:
            numbers = [int(x) for x in text.split()]
        except ValueError:
            print("Қате: тек бүтін сандарды бос орын арқылы енгізіңіз.")
            continue
        if len(numbers) < min_count:
            print(f"Қате: кемінде {min_count} сан енгізіңіз.")
            continue
        return numbers