// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDcXHG7__rzppHAbl5tD443OzDeAW56ijg",
  authDomain: "recipesharingapplication-c1752.firebaseapp.com",
  projectId: "recipesharingapplication-c1752",
  storageBucket: "recipesharingapplication-c1752.firebasestorage.app",
  messagingSenderId: "874817025185",
  appId: "1:874817025185:web:1619595c8a4b079bd8ace0",
  measurementId: "G-04EQH41NDN"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);