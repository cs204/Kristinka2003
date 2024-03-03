def feet2meter(v):
    
    feet = float(v.replace('ft', ''))
    # Переводим футы в метры (1 фут = 0.3048 метра)
    meters = feet * 0.3048
    return meters

def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

main()
