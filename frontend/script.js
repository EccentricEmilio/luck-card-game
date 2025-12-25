console.log("script.js loaded");

function getSelectedPlayers() {
    const checked = document.querySelector('input[name="players"]:checked');
    if (checked == null) {
        alert("Please select number of players to start the game.");
        throw new Error("No players selected");
    }
    return Number(checked.value);
}

document.getElementById("start-game-btn").addEventListener("click", async () => {
    const playerCount = getSelectedPlayers();
    const response = await fetch("http://127.0.0.1:8000/start_game?player_count=" + playerCount.toString());
    const data = await response.json();
    renderHands(data, playerCount)
    console.log(data)
    console.log("Game started with " + playerCount + " players.");
});



function renderHands(newHands, playerCount) {
    const container = document.querySelector(".hands-container");
    if (!container) throw new Error('Expected .hands-container in HTML');
    container.innerHTML = ""; // Clear existing hands

    for (let i = 1; i <= playerCount; i++) {
        const handDiv = document.createElement("div");
        handDiv.className = "hand";
        handDiv.id = "hand" + i.toString();

        const playedTitle = document.createElement("p");
        playedTitle.className = "hand-title";
        playedTitle.textContent = "Played cards";

        const playedDiv = document.createElement("div");
        playedDiv.className = "played-cards";
        // leave empty for now (or fill from newHands if you add that data)

        const playerTitle = document.createElement("p");
        playerTitle.className = "hand-title";
        playerTitle.textContent = `Player ${i}`;

        const holding = document.createElement("div");
        holding.className = "holding-cards";
        holding.id = `hand-${i}-holding-cards`;

        const cards = newHands[`player-${i}`];
        for (const card of cards) {
            const c = document.createElement("div");
            c.className = "card";
            c.textContent = card;
            holding.appendChild(c);
        }
        
        
        handDiv.appendChild(playedTitle);
        handDiv.appendChild(playedDiv);
        handDiv.appendChild(playerTitle);
        handDiv.appendChild(holding);
        container.appendChild(handDiv);
    }
}
    
    
    
    
    
    
    /*
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

*/




