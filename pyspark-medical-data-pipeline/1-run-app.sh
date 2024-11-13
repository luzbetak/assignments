#!/bin/bash

while true; do
    clear
    echo "==============================================="
    echo "          Medical Data Processing Menu         "
    echo "==============================================="
    echo "1. Run Application"
    echo "2. Run Tests"
    echo "3. Install Dependencies"
    echo "4. Exit"
    echo "==============================================="
    echo -n "Please enter your choice [1-4]: "
    
    read choice

    case $choice in
        1)
            echo "Running application..."
            python3 src/app.py data/eligibility.csv data/medical.csv
            echo -e "\nPress Enter to continue..."
            read
            ;;
        2)
            echo "Running tests..."
            py.test -p no:warnings
            echo -e "\nPress Enter to continue..."
            read
            ;;
        3)
            echo "Installing dependencies..."
            pip3 install -r requirements.txt
            echo -e "\nPress Enter to continue..."
            read
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please try again."
            echo "Press Enter to continue..."
            read
            ;;
    esac
done
