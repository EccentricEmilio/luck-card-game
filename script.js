const button = document.getElementById("deal");
const output = document.getElementById("output");

button.addEventListener("click", async () => {
    const response = await fetch("http://localhost:8000/ai-move", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            num_cards: 3
        })
    });

    const data = await response.json();
    output.textContent = JSON.stringify(data, null, 2);
});