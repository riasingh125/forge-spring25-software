import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.tsx";
import { FlowProvider } from "./context/FlowContext.tsx";
import { FormProvider } from "./context/FormContext.tsx";

createRoot(document.getElementById("root")!).render(
  <FormProvider>
    <FlowProvider>
      <StrictMode>
        <App />
      </StrictMode>
    </FlowProvider>
  </FormProvider>
);
