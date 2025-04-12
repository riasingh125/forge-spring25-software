import axios from "axios";

interface RankingsType {
  [key: string]: number;
}

interface FormDataType {
  firstName: string;
  lastName: string;
  email: string;
  familiarity: string;
  city: string;
  state: string;
  zip: string;
  country: string;
  salary: string;
  numHousehold: string;
  budget: string;
  concerns: string;
  rankings: RankingsType;
  files: File[];
  costs: number[];
}

function structureToJSON(data: FormDataType) {
  return {
    first_name: data.firstName || "",
    last_name: data.lastName || "",
    age: 25,
    income: parseFloat(data.salary) || 0,
    budget: parseFloat(data.budget) || 0,
    coverage: {
      ages_of_people_needing_coverage: [1, 2, 3, 4, 5],
      personal_health_concerns: data.concerns || "",
      budget: parseFloat(data.budget) || 0,
    },
    contact: {
      email: data.email || "",
      number: "0000000000",
    },
    address: {
      city: data.city || "",
      state: data.state || "",
      country: data.country || "",
      zip_code: data.zip || "",
    },
    weights: {
      affordability: data.rankings["Affordability"] || 0,
      coverage_of_all_benefits: data.rankings["Coverage of All Benefits"] || 0,
      personalized_coverage:
        data.rankings["Coverage of Personal Health Concerns"] || 0,
      flexibility_of_coverage: data.rankings["Plan Flexibility"] || 0,
      emergency_coverage: data.rankings["Coverage in Emergencies"] || 0,
      convenience_of_coverage:
        data.rankings["Convenience of Accessing Benefits"] || 0,
      geographic_coverage: data.rankings["Geographic coverage"] || 0,
    },
    premium: data.costs,
  };
}

async function sendInputData(formData: FormDataType) {
  console.log("Post request");
  try {
    const payload = new FormData();
    const jsonData = structureToJSON(formData);

    payload.append("form_data", JSON.stringify(jsonData));

    formData.files.forEach((file, index) => {
      payload.append("files", file);
      payload.append("plan_cost", String(formData.costs[index] || 0));
    });

    const response = await axios.post(
      "http://127.0.0.1:8000/form/submit",
      payload
    );

    console.log("Server response:", response.data);
    return response.data;
  } catch (error) {
    console.error(error);
    return [];
  }
}

export { sendInputData };
