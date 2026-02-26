/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docs: [
    // Getting started
    {
      type: 'category',
      label: 'Getting started',
      collapsed: false,
      items: ['intro', 'about', 'vision', 'glossary'],
    },
    // Core Thesis
    {
      type: 'category',
      label: 'Core Thesis',
      items: [{ type: 'doc', id: 'thesis/framework', label: 'Mathematics as the Nervous System of AI' }],
    },
    // RFS (core tech)
    {
      type: 'category',
      label: 'Resonant Field Storage (RFS)',
      link: { type: 'doc', id: 'rfs/overview' },
      items: [
        'rfs/overview',
        'rfs/field-theory',
        {
          type: 'category',
          label: 'Use Cases',
          link: { type: 'doc', id: 'rfs/use-cases/overview' },
          items: [
            'rfs/use-cases/overview',
            'rfs/use-cases/incident-memory',
            'rfs/use-cases/rag-proofs',
            'rfs/use-cases/code-intelligence',
            'rfs/use-cases/compliance-legal',
            'rfs/use-cases/research-knowledge',
            'rfs/use-cases/pharmaceutical',
          ],
        },
      ],
    },
    // Methodology
    {
      type: 'category',
      label: 'Methodology',
      items: ['mathematical-autopsy/overview'],
    },
    // Advisory
    {
      type: 'category',
      label: 'Advisory',
      link: { type: 'doc', id: 'advisory/README' },
      items: [
        'advisory/overview',
        'advisory/methodology',
        'advisory/guarantees',
        {
          type: 'category',
          label: 'Services',
          items: [
            'advisory/services/express-assessment',
            'advisory/services/readiness-assessment',
            'advisory/services/strategy-roadmap',
            'advisory/services/pilot-implementation',
            'advisory/services/advisor-retainer',
          ],
        },
        {
          type: 'category',
          label: 'Industry Verticals',
          items: [
            'advisory/verticals/healthcare',
            'advisory/verticals/professional-services',
            'advisory/verticals/property-real-estate',
          ],
        },
        'advisory/self-service',
      ],
    },
    // Archetypes (what we build)
    {
      type: 'category',
      label: 'Archetypes',
      items: [
        'archetypes/tai',
        'archetypes/aiva',
        'archetypes/mge',
      ],
    },
  ],
};

module.exports = sidebars;
