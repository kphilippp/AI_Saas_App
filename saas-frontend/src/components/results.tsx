import KeyWordItem from "./keywordItem";

interface ResultsProps {
  keywords: string[];
  snippet: string;
}

const Results: React.FC<ResultsProps> = (props) => {
  return (
    <div className="flex flex-col justify-between h-[40%] w-[450px]  bg-white p-8 rounded-lg shadow-lg">
      <div>
        <h1
          className="font-bold text-lg text-[var(--pmText)] mb-3"
          style={{ fontFamily: "var(--font-gs)" }}
        >
          Brand Snippet
        </h1>
        <h2
          className="text-md  text-gray-800"
          style={{ fontFamily: "var(--font-gambetta)" }}
        >
          {props.snippet}
        </h2>
      </div>
      <div>
        <h1
          className="font-bold text-lg text-[var(--pmText)] mb-3"
          style={{ fontFamily: "var(--font-gs)" }}
        >
          SEO Keywords
        </h1>
        <div
          className="flex gap-1 flex-wrap"
          style={{ fontFamily: "var(--font-gambetta)" }}
        >
          {props.keywords.map((keyword) => (
            <KeyWordItem key={keyword} keyword={keyword} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Results;
