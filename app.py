@app.route("/generate", methods=["POST"])
def generate_comic():
    data = request.get_json()
    idea = data.get("idea", "")

    prompt = f"""
    Create a comic based on this story idea:

    {idea}

    Create exactly 5 comic panels.

    Return the result in this format:

    TITLE:
    [comic title]

    PANEL 1:
    SCENE:
    [scene description]
    CHARACTERS:
    [characters]
    DIALOGUE:
    [dialogue]

    PANEL 2:
    SCENE:
    [scene description]
    CHARACTERS:
    [characters]
    DIALOGUE:
    [dialogue]

    PANEL 3:
    SCENE:
    [scene description]
    CHARACTERS:
    [characters]
    DIALOGUE:
    [dialogue]

    PANEL 4:
    SCENE:
    [scene description]
    CHARACTERS:
    [characters]
    DIALOGUE:
    [dialogue]

    PANEL 5:
    SCENE:
    [scene description]
    CHARACTERS:
    [characters]
    DIALOGUE:
    [dialogue]
    """

    response = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    return jsonify({
        "comic": response.output_text
    })
