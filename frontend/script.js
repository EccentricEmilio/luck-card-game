console.log("script.js loaded");

document.getElementById("start-game-btn").addEventListener("click", async () => {
    const response = await fetch("http://127.0.0.1:8000/ai-move", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({})
    });

    const data = await response.json();
    console.log(data)
    renderHands(data);
});

function renderHands(newHands) {
    // Make a list of all hands
    let curHands = {
        "hand-1": document.getElementById("hand-1"), 
        "hand-2": document.getElementById("hand-2"), 
        "hand-3": document.getElementById("hand-3")
    };
        

    // Clear content for each hands holding cards
    Object.keys(curHands).forEach(key => {
        curHands[key].innerHTML = "";
    });

    // Populate each hand with new cards
    for (const key in newHands) {
        newHands[key].forEach(card => {
            let div = document.createElement("div");
            div.textContent = card;
            div.className = "card";
            curHands[key].appendChild(div);
        });
    }
}




