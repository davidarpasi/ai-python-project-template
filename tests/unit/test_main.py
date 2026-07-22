from ai_python_project_template.__main__ import main


def test_main_prints_ready_message(capsys) -> None:
    main()

    captured = capsys.readouterr()

    assert captured.out == "AI Python Project Template is ready.\n"
