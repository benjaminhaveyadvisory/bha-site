// Single source of truth for awards & nominations.
// Used by /recognition/ (full record) and the homepage strip (headline: true).
export type Honor = {
  year: number;
  body: string;        // awarding body
  category: string;    // category / result detail
  result: "Winner" | "Nominee" | "Finalist";
  headline?: boolean;  // surfaces on the homepage strip
};

export type Project = {
  name: string;
  org: string;         // studio / partners, shown under the project name
  honors: Honor[];
};

export const projects: Project[] = [
  {
    name: "MobiTV",
    org: "MobiTV · Sprint",
    honors: [
      { year: 2005, body: "Primetime Emmy Awards", category: "Engineering Award — the first ever awarded to a wireless company", result: "Winner", headline: true },
    ],
  },
  {
    name: "Coco VR",
    org: "Disney · Pixar",
    honors: [
      { year: 2018, body: "Emmy Awards", category: "Outstanding Original Interactive Program", result: "Nominee", headline: true },
      { year: 2018, body: "Clio Entertainment Awards", category: "Grand Award — Digital/Mobile Virtual/Augmented Reality", result: "Winner" },
      { year: 2018, body: "Cannes Lions", category: "Silver Lion", result: "Winner", headline: true },
      { year: 2018, body: "VR Awards", category: "VR Marketing Campaign of the Year", result: "Winner" },
    ],
  },
  {
    name: "Star Wars: Secrets of the Empire",
    org: "Lucasfilm · ILMxLAB · The VOID",
    honors: [
      { year: 2018, body: "VR Awards", category: "Best Out-of-Home Experience", result: "Winner" },
      { year: 2018, body: "Visual Effects Society Awards", category: "Outstanding Visual Effects in a Special Venue Project", result: "Nominee" },
    ],
  },
  {
    name: "Vader Immortal: A Star Wars VR Series",
    org: "Disney · Lucasfilm · ILMxLAB",
    honors: [
      { year: 2019, body: "Primetime Emmy Awards", category: "Outstanding Innovation in Interactive Media", result: "Finalist" },
      { year: 2019, body: "VR Awards", category: "VR Experience of the Year — Episode I", result: "Winner" },
      { year: 2020, body: "Producers Guild of America Awards", category: "Inaugural PGA Innovation Award — Episode I", result: "Winner", headline: true },
      { year: 2020, body: "Game Developers Choice Awards", category: "Best VR/AR Game", result: "Winner" },
    ],
  },
  {
    name: "Avengers: Damage Control",
    org: "Marvel · ILMxLAB · The VOID",
    honors: [
      { year: 2020, body: "VR Awards (AIXR)", category: "Out-of-Home VR Entertainment of the Year", result: "Winner" },
      { year: 2020, body: "Visual Effects Society Awards", category: "Outstanding Visual Effects in a Special Venue Project", result: "Nominee" },
    ],
  },
  {
    name: "Focus Features",
    org: "NBCUniversal · focusfeatures.com",
    honors: [
      { year: 2024, body: "Webby Awards", category: "Desktop & Mobile Sites — Television, Film & Streaming", result: "Nominee", headline: true },
    ],
  },
];

export const allHonors = projects.flatMap((p) => p.honors.map((h) => ({ ...h, project: p.name })));
export const headlineHonors = allHonors.filter((h) => h.headline).sort((a, b) => a.year - b.year);
export const counts = {
  honors: allHonors.length,
  wins: allHonors.filter((h) => h.result === "Winner").length,
  projects: projects.length,
};

export type Patent = { title: string; number: string; url: string };
export const patents: Patent[] = [
  { title: "Machine-learning, user-specific evaluations", number: "US 11,610,239", url: "https://patents.google.com/patent/US11610239B2" },
  { title: "Drones generating air-flow effects for VR / AR users", number: "US 10,777,008", url: "https://patents.google.com/patent/US10777008B2" },
  { title: "Personalized video featuring a selected person", number: "US 10,311,917", url: "https://patents.google.com/patent/US10311917B2" },
  { title: "Graph-based content browsing & discovery", number: "US 10,671,670", url: "https://patents.google.com/patent/US10671670B2" },
  { title: "Improved augmented reality content delivery", number: "US 10,665,023", url: "https://patents.google.com/patent/US10665023B2" },
  { title: "Adjusting user experience based on biological response", number: "US 10,394,324", url: "https://patents.google.com/patent/US10394324B2" },
  { title: "AR / VR digital content representation & interaction", number: "US 10,269,158", url: "https://patents.google.com/patent/US10269158B2" },
  { title: "Simulation experience with physical objects", number: "US 10,627,909", url: "https://patents.google.com/patent/US10627909B2" },
  { title: "Modeling lighting for location scouting", number: "US 10,140,754", url: "https://patents.google.com/patent/US10140754B1" },
  { title: "Home entertainment content & enhanced ticketing", number: "App. 2025/0209435", url: "https://patents.google.com/patent/US20250209435A1" },
];
