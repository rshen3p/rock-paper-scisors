from io import StringIO
import src.game as game


def test_get_user_input_rock(monkeypatch):
    user_input = StringIO('r\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.get_user_input() == 'r'


def test_get_user_input_paper(monkeypatch):
    user_input = StringIO('p\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.get_user_input() == 'p'


def test_get_user_input_scissor(monkeypatch):
    user_input = StringIO('s\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.get_user_input() == 's'


def test_get_user_input_invalid_short_number_inputs(monkeypatch):
    user_input = StringIO('1\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.get_user_input() == 'invalid'


def test_get_user_input_invalid_long_number_inputs(monkeypatch):
    user_input = StringIO('12399999999999999999999999999999999999999999999111111111111123\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.get_user_input() == 'invalid'


def test_get_user_input_invalid_special_character_inputs(monkeypatch):
    user_input = StringIO('#/\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.get_user_input() == 'invalid'


def test_get_user_input_invalid_empty_inputs(monkeypatch):
    user_input = StringIO('\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.get_user_input() == 'invalid'


def test_convert_input_rock():
    assert game.convert_input('r') == 'rock'


def test_convert_input_paper():
    assert game.convert_input('p') == 'paper'


def test_convert_input_scissor():
    assert game.convert_input('s') == 'scissor'


def test_compare_input_rock_beat_scissor(capfd):
    game.compare_input('r', 's')
    out, err = capfd.readouterr()
    assert out == "\nUser has WON! User used rock to beat scissor\n\n"


def test_compare_input_paper_beat_rock(capfd):
    game.compare_input('p', 'r')
    out, err = capfd.readouterr()
    assert out == "\nUser has WON! User used paper to beat rock\n\n"


def test_compare_input_scissor_beat_paper(capfd):
    game.compare_input('s', 'p')
    out, err = capfd.readouterr()
    assert out == "\nUser has WON! User used scissor to beat paper\n\n"


def test_compare_input_scissor_lose_to_rock(capfd):
    game.compare_input('s', 'r')
    out, err = capfd.readouterr()
    assert out == "\nUser has LOST! Computer used rock to beat scissor\n\n"


def test_compare_input_rock_lose_to_paper(capfd):
    game.compare_input('r', 'p')
    out, err = capfd.readouterr()
    assert out == "\nUser has LOST! Computer used paper to beat rock\n\n"


def test_compare_input_paper_lose_to_scissor(capfd):
    game.compare_input('p', 's')
    out, err = capfd.readouterr()
    assert out == "\nUser has LOST! Computer used scissor to beat paper\n\n"


def test_compare_input_paper_ties_paper(capfd):
    game.compare_input('p', 'p')
    out, err = capfd.readouterr()
    assert out == "\nBoth user and the computer chose paper, so this round is a tie!\n\n"


def test_compare_input_scissor_ties_scissor(capfd):
    game.compare_input('s', 's')
    out, err = capfd.readouterr()
    assert out == "\nBoth user and the computer chose scissor, so this round is a tie!\n\n"


def test_compare_input_rock_ties_rock(capfd):
    game.compare_input('r', 'r')
    out, err = capfd.readouterr()
    assert out == "\nBoth user and the computer chose rock, so this round is a tie!\n\n"


def test_is_continue_yes(monkeypatch):
    user_input = StringIO('y\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.is_continue() == True


def test_is_continue_no(monkeypatch):
    user_input = StringIO('n\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.is_continue() == False


def test_is_continue_invalid_short_number_input(monkeypatch):
    user_input = StringIO('1\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.is_continue() == False


def test_is_continue_invalid_long_number_input(monkeypatch):
    user_input = StringIO('111111111111111111111111111111111111111111111111111111111111111111111111111111111111\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.is_continue() == False


def test_is_continue_invalid_short_character_input(monkeypatch):
    user_input = StringIO('v\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.is_continue() == False


def test_is_continue_invalid_long_character_input(monkeypatch):
    user_input = StringIO('vhasjkdhewiuryjsabdfkbasdffuiiujsadjkfhasdjk\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.is_continue() == False


def test_is_continue_invalid_special_character_input(monkeypatch):
    user_input = StringIO('#$@!%\n')
    monkeypatch.setattr('sys.stdin', user_input)
    assert game.is_continue() == False

