import axios from "axios";

interface FormDataInput {
  firstName: string;
  lastName: string;
  age: string;
  salary: string;
  budget: string;
  concerns: string;
  email: string;
  phone: string;
  city: string;
  state: string;
  country: string;
  zip: string;
  [key: string]: any;
}

function structureToJSON(data: FormDataInput, planCost: number[]) {

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
            "coverage_of_all_benefits": parseFloat(data["Coverage of All Benefits"]) || 0,
            "personalized_coverage": parseFloat(data["Coverage of Personal Health Concerns"]) || 0,
            "flexibility_of_coverage": parseFloat(data["Plan Flexibility"]) || 0,
            "emergency_coverage": parseFloat(data["Coverage in Emergencies"]) || 0,
            "convenience_of_coverage": parseFloat(data["Convenience of Accessing Benefits"]) || 0,
            "geographic_coverage": parseFloat(data["Geographic coverage"]) || 0,
        },
        "premium" : planCost
    };
}

/**
 * POST request to backend to send user input and get back results
 * @param data the user's filled out form data
 * @param files the uploaded pdfs of the insurance plans
 */
async function sendInputData(data: FormDataInput, files: File[], planCost: number[]) {
    console.log("Post request");
  try {
    const formData = new FormData();
    // add the user form data
    const jsonData = structureToJSON(data, planCost);

    formData.append("form_data", JSON.stringify(jsonData));
    // add all the uploaded files
    files.forEach((file) => {
      formData.append("files", file);
      formData.append("plan_cost", String(planCost[files.indexOf(file)]));
    });
    const response = await axios.post(
      "http://127.0.0.1:8000/form/submit",
      formData
    );
    console.log("Server response:", response.data);
    return response.data;
  } catch (error) {
    console.error("Submission error:", error);
    if (axios.isAxiosError(error) && error.response) {
      // 422 - incorrect format
      console.error("Error status:", error.response?.status);
      alert(
        `Error submitting the form: ${
          error.response.data.detail || "Unknown error"
        }`
      );
    } else {
      alert("Failed to connect to the server.");
    }

    return [];

  }
}

export { sendInputData };
