import axios from "axios";

export async function getResults() {
    try {
        const response = await axios.get("http://127.0.0.1:8000/results", {
            headers: { "Content-Type": "application/json" }
        });
        return response.data.results;
    } catch (error) {
        console.error("Get error:", error);

        if (axios.isAxiosError(error) && error.response) {
            alert(`Error: ${error.response.data.detail || "Failed to get results"}`);
        } else {
            alert("Failed to connect to the server.");
        }
    }
}
