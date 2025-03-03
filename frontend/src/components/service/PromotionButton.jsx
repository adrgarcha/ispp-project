export default function PromotionButton({ type, text, icon, onClick, isError, errorMessage }) {
    return (
        <div className="flex justify-center">
            <button type={type} className="flex items-center gap-x-2 p-2 border bg-orange-200 rounded-lg hover:bg-gray-200 transition" onClick={onClick}>
                {icon}
                {text}
            </button>
            {isError && <p className="pl-1 text-red-500 text-xs">{errorMessage}</p>}
        </div>
        )
    }