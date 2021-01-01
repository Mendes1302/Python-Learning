def maior(* value):
    m = 0
    print("="*40)
    print("\nAnalisando os valores: ")
    for i in value:
        print(f"{i}", end=' ')
        if i > m:
            m = i
    print(f"\n\nCONCLUSÃO\nO maior  valor é {m}")
    print("="*40)

maior(0,5,9,78,1,200)
maior(0,5,9)
maior(9,78,1,200)

        
