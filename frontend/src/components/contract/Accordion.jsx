import { useState } from "react";

const Accordion = ({title, answer}) => {

    const [isOpen, setIsOpen] = useState(false);
    return (
        <div className="py-2">

            <button onClick={() => setIsOpen(!isOpen)} className="flex justify-between w-full">
                <span>{title}</span>
                <svg
                    className="fill-indigo-500 shrink-0 ml-8"
                    width="16"
                    height="16"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <rect
                        y="7"
                        width="16"
                        height="2"
                        rx="1"
                        className={`transform origin-center transition duration-200 ease-out ${isOpen && "!rotate-180"
                            }`}
                    />
                    <rect
                        y="7"
                        width="16"
                        height="2"
                        rx="1"
                        className={`transform origin-center rotate-90 transition duration-200 ease-out ${isOpen && "!rotate-180"
                            }`}
                    />
                </svg>

            </button>
            <div className={`grid overflow-hidden transition-all duration-300 ease-in-out text-slate-600 text-s ${isOpen
                ? 'grid-rows-[1fr] opacity-100'
                : 'grid-rows-[0fr] opacity-0'
                }`}>
                <div className="overflow-hidden">
                    <p dangerouslySetInnerHTML={{ __html: answer }}></p>
                </div>
            </div>
        </div>

    )

};

export default Accordion;