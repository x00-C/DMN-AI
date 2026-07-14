class LocalVectorVault:
    """
    Manages clinical metrics for multiple distinct patient profiles.
    Switches datasets dynamically based on active UI selections.
    """
    def __init__(self, target_patient="Patient 1 (ADHD)"):
        self.target_patient = target_patient

    def retrieve_session_payloads(self):
        if "Patient 1" in self.target_patient:
            transcript = (
                "Patient (24yo Male): \"I just... I can't seem to finish anything lately. "
                "I sit down to read or study for my midterms, and within two minutes, my mind "
                "is completely somewhere else. My keys are always missing. My roommates say "
                "I'm always interrupting them, but I don't even notice I'm doing it. I try really "
                "hard to sit still, but it feels like my engine is constantly revving inside.\""
            )
            biometric_vectors = (
                "Local Keyframe Coordinates:\n"
                "- Timestamp 00:15 - 01:30: Spatial hand tracking coordinates map high-amplitude variance. "
                "Frequent kinetic gesticulations correlate directly with verbal focus declarations.\n"
                "- Timestamp 01:45: Rapid core posture adjustment changes detected at 8/min "
                "(Baseline control threshold: < 2).\n"
                "- Continuous: Persistent oculomotor micro-fixation changes indicate underlying cognitive strain."
            )
        else:
            # Patient 2 (Anxiety) high-fidelity clinical dataset profiles
            transcript = (
                "Patient (31yo Female): \"My chest constantly feels tight, like I cannot take a full breath. "
                "The dread starts the moment I wake up and follows me all day. I am constantly reviewing "
                "every conversation I had during the week, convinced I said something wrong. I just want "
                "my mind to stop racing for a single hour so I can rest.\""
            )
            biometric_vectors = (
                "Local Keyframe Coordinates:\n"
                "- Timestamp 00:45 - 02:10: Micro-oscillations tracking around the thoracic region "
                "confirm restrictive, shallow intercostal respiratory cycles.\n"
                "- Timestamp 01:20: Tremor metrics localized across bilateral manual tracking parameters (Frequency: 7.5Hz).\n"
                "- Continuous: Tonic muscular contractions detected along neck and trapezius vector groups."
            )
            
        return transcript, biometric_vectors