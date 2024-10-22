import KeyWordItem from "./keywordItem";

interface ResultsProps {
  keywords: string[];
  snippet: string;
}

const Results: React.FC<ResultsProps> = (props) => {
  return (
    <div className="flex flex-col justify-evenly h-[40%] w-[450px]  bg-white p-8 rounded-lg shadow-lg">
      <div>
        <h1 className="font-bold text-lg text-[var(--pmText)] mb-3">
          Brand Snippet
        </h1>
        <h2 className="text-md italic text-gray-800">{props.snippet}</h2>
      </div>
      <div>
        <h1 className="font-bold text-lg text-[var(--pmText)] mb-3">
          SEO Keywords
        </h1>
        <div className="flex gap-1 flex-wrap">
          {props.keywords.map((keyword) => (
            <KeyWordItem key={keyword} keyword={keyword} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default Results;
