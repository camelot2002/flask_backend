document
  .getElementById("queryForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    const queryInput = document.getElementById("chequeQuery");
    const queryResult = document.getElementById("queryResult");
    const userQuery = queryInput.value;

    const data = {
      query: userQuery,
    };

    fetch("http://localhost:5000/query", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.text();
      })
      .then((result) => {
        const formattedResult = result.split("\\n").join("\n").replace(/[\[\]"]/g, "").replace(/,/g, "");
        queryResult.innerText = formattedResult;
      })
      .catch((error) => {
        console.error("Error:", error);
        queryResult.innerHTML = `<p>Something went wrong. Please try again.</p>`;
      });

    queryInput.value = "";
  });
