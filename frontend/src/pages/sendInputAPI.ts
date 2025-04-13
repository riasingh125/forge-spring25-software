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
  numHousehold: string;
  state: string;
  country: string;
  zip: string;
  [key: string]: any;
}

function structureToJSON(data: FormDataInput, planCost: number[]) {
  const weights = data["weights"];
  return {
    first_name: data.firstName || "",
    last_name: data.lastName || "",
    age: parseInt(data.age) || 25,
    income: parseFloat(data.salary) || 0,
    budget: parseFloat(data.budget) || 0,
    coverage: {
      household_size: parseInt(data.numHousehold) || 1,
      personal_health_concerns: data.concerns || "",
      budget: parseFloat(data.budget) || 0,
    },
    contact: {
      email: data.email || "",
      number: data.phone || "0000000000",
    },
    address: {
      city: data.city || "",
      state: data.state || "",
      country: data.country || "",
      zip_code: data.zip || "",
    },
    weights: {
      affordability: parseFloat(weights["Affordability"]) || 1,
      coverage_of_all_benefits:
        parseFloat(weights["Coverage of All Benefits"]) || 1,
      personalized_coverage:
        parseFloat(weights["Coverage of Personal Health Concerns"]) || 1,
      flexibility_of_coverage: parseFloat(weights["Plan Flexibility"]) || 1,
      emergency_coverage: parseFloat(weights["Coverage in Emergencies"]) || 1,
      convenience_of_coverage:
        parseFloat(weights["Convenience of Accessing Benefits"]) || 1,
      geographic_coverage: parseFloat(weights["Geographic coverage"]) || 1,
    },
    premium: planCost,
  };
}

/**
 * POST request to backend to send user input and get back results
 * @param data the user's filled out form data
 * @param files the uploaded pdfs of the insurance plans
 */
async function sendInputData(
  data: FormDataInput,
  files: File[],
  planCost: number[]
) {
  console.log("Post request");
  console.log("DATA CHECK:");
  console.log(data);
  try {
    const formData = new FormData();
    // add the user form data
    const jsonData = structureToJSON(data, planCost);

    console.log("JSON DATA CHECK:");
    console.log(jsonData);

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
    console.log(error);
    return [];
  }
}

export { sendInputData };
