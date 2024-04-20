export async function checkIfUsernameExists(username, userId) {
    const res = await fetch(`${import.meta.env.VITE_BACKEND_API_URL}/user/`);
    const data = await res.json();
    const filteredData = data.filter(existingUser => existingUser.id !== userId && existingUser.username === username);
    return filteredData.length > 0;
}

export function checkIfEmpty(text) {
    return text.trim().length === 0;
}
export function checkUsernameIfEmptyAndSize(username){
    return !username.trim() || username.length < 3 || username.length >= 31;
}
export function checkFirstNameIfEmptyAndSize(firstName){
    return !firstName.trim() || firstName.length < 3 || firstName.length >= 31;
}

export function checkLastNameIfEmptyAndSize(lastName){
    return !lastName.trim() || lastName.length < 3 || lastName.length >= 61;
}

export function checkOnlyCharactersInText(text) {
    const onlyCharactersRegex = /^[a-zA-ZñÑáéíóúÁÉÍÓÚüÜç '`´]+$/;
    return !onlyCharactersRegex.test(text);
}

export function checkCityLength(city) {
    return city.length > 50;
}

export function checkExperienceNegative(experience) {
    return experience < 0;
}

export function checkProfessionDuplicated(profession, professions) {
    return professions.includes(profession);
}

export function checkExperienceYears(experience, userBirthDate) {
    const age = getAge(userBirthDate);
    return Number(experience) + 16 > age;
}

export function checkIfImage(file) {
    return !file.type.startsWith("image/");
}

export function checkIfDateInFuture(date) {
    return new Date(date) > new Date();
}

export function checkIfBirthDateValid(date) {
    const age = getAge(date);
    return !(age > 16 && age < 80);
}

export function checkIfPointsPositive(points) {
    return points < 0;
}

export function checkIfToManyPoints(yourPoints, pointsUsed) {
    return yourPoints < pointsUsed;
}

export function checkIfPointsMoreThanMoney(points, money) {
    // Hay un minimo de 0,50€ en Stripe, por eso al precio total se le resta 50 centimos
    return points > ((money * 100)-50);
}

export const errorMessages = {
    required: "Este campo es requerido.",
    cityLength: "La ciudad no debe tener más de 50 caracteres.",
    experienceNotValid: "La experiencia no puede ser menos que 0.",
    tooMuchExperience: "La experiencia no puede ser tan grande en comparación con la edad del usuario.",
    languageLength: "El idioma no debe tener más de 50 caracteres.",
    imageNotValid: "La imagen no es válida.",
    emailNotValid: "El correo electrónico no es válido.",
    usernameExists: "El nombre de usuario ya existe.",
    professionDuplicate: "No se pueden crear dos servicios con la misma profesión.",
    onlyCharacters: "Este campo solo puede contener letras.",
    dateInFuture: "La fecha no puede estar en el futuro.",
    birthDateNotValid: "Debes tener más de 16 años y menos de 80 años.",
    tooManyPoints: "Por favor, introduzca una cantidad de puntos que tengas disponibles.",
    positivePoints: "Por favor, introduzca un número de puntos positivos.",
    noMorePointsMoney: "El pago debe ser mínimo de 0'50€. No puedes canjear más puntos si eso hace que el precio sea menor de 0'50€.",
    usernameRequiredAndSize: "El nombre de usuario debe ser menos de 30 caracteres, mas de 3 y no debe estar en blanco",
    nameRequiredAndSize: "El nombre de usuario debe ser menos de 30 caracteres, mas de 3 y no debe estar en blanco",
    lastnameRequiredAndSize: "El nombre de usuario debe ser menos de 30 caracteres, mas de 3 y no debe estar en blanco",
}

function getAge(date) {
    const today = new Date();
    const birthDate = new Date(date);
    let age = today.getFullYear() - birthDate.getFullYear();
    const month = today.getMonth() - birthDate.getMonth();
    if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
}