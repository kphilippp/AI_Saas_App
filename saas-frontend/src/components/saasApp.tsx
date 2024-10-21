"use client";

import React from "react";

const SaasApp: React.FC = () => {
  //You are fecthing from the endpoint that apiGateway gave us and we
  //are speciifying the endpoint to get an appropriate res
  const AWS_ENDPOINT_BEFORE: string =
    "https://aawc0obe06.execute-api.us-west-2.amazonaws.com/prod";
  const [prompt, setPrompt] = React.useState("");
  const [keywords, setKeywords] = React.useState([]);
  const [snippet, setSnippet] = React.useState(``);
  const [hasResults, setHasResults] = React.useState(false);

  const handleSubmit = () => {
    fetch(`${AWS_ENDPOINT_BEFORE}/snippet_keywords?msg=${prompt}`)
      .then((res) => res.json())
      .then((data) => {
        setKeywords(data.keywords);
        setSnippet(data.snippet);
        setHasResults(true);
      });
  };

  return (
    <>
      <h1>Saas App</h1>
      <p>Tell me what your brand is about</p>

      {hasResults && <div>{snippet}</div>}

      <input
        type="text"
        placeholder="coffee"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      <button onClick={handleSubmit}>Submit</button>
    </>
  );
};

export default SaasApp;
