import axios from "axios";


function structureToJSON(data) {

    return {
        "first_name": data.firstName || "",
        "last_name": data.lastName || "",
        "age": parseInt(data.age) || 25,
        "income": parseFloat(data.salary) || 0,
        "budget": parseFloat(data.budget) || 0,
        "coverage": {
            "ages_of_people_needing_coverage": [1, 2, 3, 4, 5],
            "personal_health_concerns": data.concerns || "",
            "budget": parseFloat(data.budget) || 0
        },
        "contact": {
            "email": data.email || "",
            "number": data.phone || "0000000000"
        },
        "address": {
            "city": data.city || "",
            "state": data.state || "",
            "country": data.country || "",
            "zip_code": data.zip || ""
        },
        "weights": {
            "affordability": parseFloat(data["Affordability"]) || 0,
            "health_concerns": parseFloat(data["Personal Health Concerns"]) || 0,
            "essential_services": parseFloat(data["Coverage of Essential Services"]) || 0,
            "plan_flexibility": parseFloat(data["Plan Flexibility"]) || 0,
            "geographic_coverage": parseFloat(data["Geographic Coverage"]) || 0,
            "dependencies": parseFloat(data["Coverage for Family and Dependents"]) || 0,
            "convenience": parseFloat(data["Convenience/Ease of Use"]) || 0,
            "long_term_benefits": parseFloat(data["Long-Term Benefits"]) || 0
        }
    };
}

/**
 * POST request to backend to send user input and get back results
 * @param data the user's filled out form data
 * @param files the uploaded pdfs of the insurance plans
 */
async function sendInputData(data: object, files: File[]) {
    try {
        console.log('Trying POST Request to backend')
        const formData = new FormData();
        // add the user form data
        data = structureToJSON(data)
        formData.append("form_data", JSON.stringify(data));
        // add all the uploaded files
        files.forEach((file) => {
            formData.append("files", file);
        });
        const response = await axios.post("http://127.0.0.1:8000/form/submit", formData);
        console.log("Server response:", response.data);
        return true;
    } catch (error) {
        console.error("Submission error:", error);
        if (axios.isAxiosError(error) && error.response) {
            // 422 - incorrect format
            console.error("Error status:", error.response?.status);
            alert(`Error submitting the form: ${error.response.data.detail || "Unknown error"}`);
        } else {
            alert("Failed to connect to the server.");
        }
        return false;
    }
}


export {
    sendInputData

};
