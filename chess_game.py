import chess

def main():
    board = chess.Board()
    
    print("Шахматы")
    print("Вводите ходы в формате алгебраической нотации (например: e2e4, Nf3, O-O)")
    print("Для выхода введите 'quit'\n")
    
    while not board.is_game_over():
        print(board)
        print()
        
        turn = "Белые" if board.turn == chess.WHITE else "Чёрные"
        move_str = input(f"{turn}, ваш ход: ").strip()
        
        if move_str.lower() in ("quit", "exit", "q"):
            print("Игра прервана.")
            return
        
        try:
            move = board.parse_san(move_str)
            board.push(move)
        except ValueError:
            print("Неверный ход! Попробуйте ещё раз.\n")
    
    print(board)
    print()
    result = board.result()
    if result == "1-0":
        print("Белые победили!")
    elif result == "0-1":
        print("Чёрные победили!")
    else:
        print("Ничья!")

if __name__ == "__main__":
    main()
