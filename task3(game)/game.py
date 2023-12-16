\#!/bin/bash

hit_count=0
miss_count=0
total_count=0
numbers=()

while true; do
    ((total_count++))

    # Генерация рандомного числа
    target_number=$((RANDOM % 10))

    # Читаем что ввел пользователь
    echo -e "Step: $total_count\nPlease enter a number from 0 to 9 (q - quit): \c"
    read user_input

    # Проверка на желание выйти
    if [ "$user_input" == "q" ]; then
        echo "Game over."
        exit 0
    fi

    # Валидация введенного
    if ! [[ "$user_input" =~ ^[0-9]$ ]]; then
        echo "Invalid input. Please enter a single digit number or 'q' to quit."
        continue
    fi

    # Проверяем угадал ли пользователь число
    if [ "$user_input" -eq "$target_number" ]; then
        ((hit_count++))
        result="Hit! My number: $target_number"
        numbers=("${numbers[@]}" " \e[32m$user_input\e[0m")
    else
        ((miss_count++))
        result="Miss! My number: $target_number"
        numbers=("${numbers[@]}" " \e[31m$user_input\e[0m")
    fi

    # Считаем проценты
    if [ "$total_count" -gt 0 ]; then
        hit_percentage=$(bc <<< "scale=2; ($hit_count / $total_count) * 100")
        miss_percentage=$(bc <<< "scale=2; ($miss_count / $total_count) * 100")
    else
        hit_percentage=0
        miss_percentage=0
    fi

    # Делаем так,чтобы массив хранил последние 10 чисел
    if [ "${#numbers[@]}" -gt 10 ]; then
        numbers=("${numbers[@]:1}")
    fi

    # Выводим результат
    echo -e "$result\nHit: ${hit_percentage}% Miss: ${miss_percentage}%"

    # Выводим 10 чисел
    echo -n "Numbers:"
    for number in "${numbers[@]}"; do
        echo -en "$number"
        if [ $number != "${numbers[-1]}" ]; then
            echo -n " "
        fi
    done
    echo

done

