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

    fetch("/query", {
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
        queryResult.innerHTML = `<p>${result}</p>`;
      })
      .catch((error) => {
        console.error("Error:", error);
        queryResult.innerHTML = `<p>Something went wrong. Please try again.</p>`;
      });

    queryInput.value = "";
  });

// document.addEventListener("DOMContentLoaded", function () {
//   // Get the form and result elements
//   const queryForm = document.getElementById("queryForm");
//   const queryResult = document.getElementById("queryResult");

//   // Add event listener to the form for submission
//   queryForm.addEventListener("submit", function (event) {
//     event.preventDefault(); // Prevent the default form submission behavior

//     // Get the value of the query input
//     const queryInput = document.getElementById("chequeQuery");
//     const queryValue = queryInput.value;

//     // Perform any action or query the backend based on the queryValue
//     // For demonstration, let's just update the queryResult with the queryValue
//     queryResult.innerText = `Here You Go: \n\n ${queryValue}`;
//   });

//   // Add event listener for the "Graph Visualization" button
//   const visualizationButton = document.querySelector(".visualization-button");
//   visualizationButton.addEventListener("click", function () {
//     // Perform any action or query the backend for visualization
//     // For demonstration, let's just update the queryResult with a visualization message
//     queryResult.textContent = "Graph Visualization: Displaying Graph...";
//   });
// });
