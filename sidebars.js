/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  docs: [
    'intro',

    {
      type: 'category',
      label: 'Why SMARTHAUS',
      collapsed: false,
      items: [
        { type: 'doc', id: 'six-failures', label: 'The Six Failures' },
      ],
    },

    {
      type: 'category',
      label: 'Products',
      collapsed: false,
      items: [
        { type: 'doc', id: 'products/ucp', label: 'UCP — Universal Control Plane' },
        { type: 'doc', id: 'products/said', label: 'SAID — Deterministic Inference' },
        { type: 'doc', id: 'products/mae', label: 'MAE — Mathematical Autopsy Engine' },
      ],
    },

    {
      type: 'category',
      label: 'PALI',
      items: [
        { type: 'doc', id: 'pali', label: 'Personal AI Layer Interface' },
      ],
    },

    {
      type: 'category',
      label: 'Methodology',
      items: [
        { type: 'doc', id: 'mathematical-autopsy/overview', label: 'Mathematical Autopsy' },
        'mathematical-autopsy/how-it-works',
        'mathematical-autopsy/methodology',
      ],
    },

    {
      type: 'category',
      label: 'Substrate (RFS)',
      link: { type: 'doc', id: 'rfs/overview' },
      items: [
        'rfs/overview',
        'rfs/field-theory',
        'rfs/innovations',
        'rfs/natural-science-thesis',
        'rfs/stakeholder-overview',
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

    {
      type: 'category',
      label: 'Research',
      items: [
        { type: 'doc', id: 'research/princeton', label: 'Princeton Research' },
        { type: 'doc', id: 'research/patents', label: 'Patents' },
        { type: 'doc', id: 'thesis/framework', label: 'Math Thesis (v7)' },
      ],
    },

    {
      type: 'category',
      label: 'Advisory',
      link: { type: 'doc', id: 'advisory/README' },
      items: [
        'advisory/how-we-engage',
        'advisory/methodology',
        'advisory/overview',
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

    {
      type: 'category',
      label: 'Reference',
      items: [
        'about',
        'glossary',
      ],
    },
  ],
};

module.exports = sidebars;
